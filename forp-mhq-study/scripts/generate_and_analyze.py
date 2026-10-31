from pathlib import Path
import numpy as np, pandas as pd, json, scipy.stats as st
import statsmodels.api as sm
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.stats import norm
from numpy.linalg import eigvalsh
from sklearn.decomposition import FactorAnalysis

OUT=Path(__file__).resolve().parents[1]
for p in ['data','results','figures','manuscript','slides','scripts','protocol']: (OUT/p).mkdir(parents=True,exist_ok=True)
SEED=20261031
rng=np.random.default_rng(SEED)
n=360
pid=np.array([f'SYN-{i:04}' for i in range(1,n+1)])
age=np.clip(np.round(rng.normal(41,13,n)),18,75).astype(int)
female=rng.binomial(1,.61,n)
dx=rng.choice(['Depression','Anxiety','Bipolar','OCD','Other'],size=n,p=[.39,.31,.12,.12,.06])
dx_code=pd.Categorical(dx,categories=['Depression','Anxiety','Bipolar','OCD','Other'])
family_lat=np.clip(rng.normal(.4,.85,n),-2.1,2.2)
family_items=np.clip(np.rint(4.8+1.12*family_lat[:,None]+rng.normal(0,.9,(n,4))),1,7).astype(int)
family=np.mean(family_items,axis=1)
phq_lat=.25*(dx=='Depression')+.22*(dx=='Anxiety')-.09*family_lat+rng.normal(0,.9,n)
phq_items=np.clip(np.rint(1+0.46*phq_lat[:,None]+rng.normal(0,.7,(n,4))),0,3).astype(int)
phq4=phq_items.sum(axis=1)
stigma_lat=np.clip(rng.normal(.2-.3*family_lat,.95,n),-1.8,2.2)
stigma_item=np.clip(np.rint(2.0+1.0*stigma_lat+rng.normal(0,.7,n)),0,4).astype(int)
# Four-varying clinical consequence categorical response. Not a validated psychometric indicator.
consequence=rng.choice(['Symptoms','Family','Work','Stigma','Autonomy','Other'],n,p=[.30,.17,.18,.15,.17,.03])
fear_lat=.57*phq_lat-.30*family_lat+.29*stigma_lat+.14*(dx=='Bipolar')+rng.normal(0,.85,n)
# ordinal FORP-MHQ item codes only; no copyrighted scale item wording in dataset
load=np.array([.78,.8,.76,.82,.75,.81,.73,.77,.79,.8])
latent_items=fear_lat[:,None]*load+rng.normal(size=(n,10))*np.sqrt(1-load**2)
item=np.digitize(latent_items,[-.95,-.2,.4,1.1]).astype(int)
forp=item.sum(axis=1)
well_lat=np.clip(-.45*phq_lat-.32*fear_lat+.22*family_lat+rng.normal(0,.8,n),-2.5,2.5)
who_items=np.clip(np.rint(3.1+0.85*well_lat[:,None]+rng.normal(0,.62,(n,5))),0,5).astype(int)
who0=who_items.sum(axis=1)*4
# prospective follow up. Continuous WHO-5 in multiples of four, with baseline adjustment
# underlying true 6mo risk model intentionally pre-specified
raw_y6=52+.50*(who0-52)-.36*(forp-19)-.9*(phq4-4)+1.8*(family-4.5)-1.4*(stigma_item-2)+rng.normal(0,12.2,n)
who6=np.clip(np.rint(raw_y6/4)*4,0,100).astype(int)
raw_y3=.52*who0+.48*who6+rng.normal(0,8,n)
who3=np.clip(np.rint(raw_y3/4)*4,0,100).astype(int)
# higher symptoms & high fear -> more dropouts, modest MNAR risk -> limitation
loss_prob=1/(1+np.exp(-(-1.7+.10*(phq4-4)+.023*(forp-19)-.05*(family-4.5))))
observed6=rng.uniform(size=n)>loss_prob
observed3=rng.uniform(size=n)>(.12+.03*(phq4>=7))
# clinical deterioration: discrete synthetic event not the primary endpoint
risk=1/(1+np.exp(-(-1.75+.055*(forp-20)+.13*(phq4-4)-.24*(family-4.5))))
clinical=rng.binomial(1,risk,n)
# retest reinterview: selected 74 clinically stable participants, retain 61+ approx
stable=np.where((np.abs(who6-who0)<=24)&observed6)[0]
rng.shuffle(stable)
retest_ids=stable[:65]
retest_score=np.full(n,np.nan)
retest_score[retest_ids]=np.clip(forp[retest_ids]+np.rint(rng.normal(0,3.4,len(retest_ids))),0,40)
# adherence when prescribed medication, only baseline, not longitudinal
med=rng.binomial(1,.83,n)
# MARS lower with stigma and fear, higher family support
mars_items=np.clip(np.rint(4.4-.14*stigma_item[:,None]-.028*forp[:,None]+.20*family[:,None]+rng.normal(0,.65,(n,5))),1,5).astype(int)
mars=mars_items.sum(axis=1).astype(float);mars[med==0]=np.nan

df=pd.DataFrame(dict(id=pid,age=age,sex_female=female,diagnosis=dx,phq4=phq4,mspss_family_mean=family.round(2),stigma_concern=stigma_item,primary_feared_consequence=consequence,forp_total=forp,who5_baseline=who0,who5_m3=np.where(observed3,who3,np.nan),who5_m6=np.where(observed6,who6,np.nan),medication_prescribed=med,mars5_total=mars,clinical_deterioration_m6=np.where(observed6,clinical,np.nan),forp_retest_28d=retest_score))
for j in range(10):df[f'forp_item_{j+1:02d}']=item[:,j]
for j in range(4):df[f'family_item_{j+1}']=family_items[:,j]
for j in range(4):df[f'phq4_item_{j+1}']=phq_items[:,j]
for j in range(5):df[f'who5_item_{j+1}']=who_items[:,j]
df.to_csv(OUT/'data'/'synthetic_cohort.csv',index=False,encoding='utf-8-sig')

# calculate stats from single source of truth
complete=df.dropna(subset=['who5_m6']).copy()
# linear model as predefined using baseline WHO-5, FORP (per 10 units), PHQ4, age, sex,
# family (per scale point), stigma and diagnosis dummies, HC3 CI
complete['forp_per10']=complete.forp_total/10
Xm=complete[['forp_per10','who5_baseline','phq4','age','sex_female','mspss_family_mean','stigma_concern']].copy()
Xd=pd.get_dummies(complete['diagnosis'],prefix='dx',drop_first=True,dtype=int)
Xm=sm.add_constant(pd.concat([Xm,Xd],axis=1).astype(float))
m=sm.OLS(complete['who5_m6'],Xm).fit(cov_type='HC3')
basecols=[c for c in Xm.columns if c!='forp_per10']
mb=sm.OLS(complete['who5_m6'],Xm[basecols]).fit(cov_type='HC3')
# interaction exploratory
Xi=Xm.copy()
Xi['forp_x_family']=(complete['forp_per10']-complete['forp_per10'].mean())*(complete['mspss_family_mean']-complete['mspss_family_mean'].mean())
mi=sm.OLS(complete['who5_m6'],Xi).fit(cov_type='HC3')
# logistic secondary
Lg=complete[['forp_per10','who5_baseline','phq4','age','sex_female','mspss_family_mean','stigma_concern']].astype(float)
Lg=sm.add_constant(Lg)
logit=sm.Logit(complete.clinical_deterioration_m6,Lg).fit(disp=False)
# reliability alpha and model-based omega approximated using continuous ML FactorAnalysis (not ordinal CFA)
q=df[[f'forp_item_{j+1:02d}' for j in range(10)]].to_numpy(float)
p=q.shape[1];alpha=p/(p-1)*(1-q.var(axis=0,ddof=1).sum()/q.sum(axis=1).var(ddof=1))
standardized=(q-q.mean(axis=0))/q.std(axis=0,ddof=1)
fact=FactorAnalysis(n_components=1,random_state=SEED).fit(standardized)
lambda_=fact.components_.flatten()
if lambda_.mean()<0:lambda_=-lambda_
psi=fact.noise_variance_
omega=(lambda_.sum()**2)/(lambda_.sum()**2+psi.sum())
# retest absolute agreement ICC(A,1) via ANOVA
pairs=df.dropna(subset=['forp_retest_28d'])[['forp_total','forp_retest_28d']].to_numpy(float)
k=2;nn=len(pairs)
grand=pairs.mean(); rowmean=pairs.mean(axis=1); colmean=pairs.mean(axis=0)
ssr=k*np.square(rowmean-grand).sum();ssc=nn*np.square(colmean-grand).sum();sse=np.square(pairs-rowmean[:,None]-colmean[None,:]+grand).sum()
msr=ssr/(nn-1);msc=ssc/(k-1);mse=sse/((nn-1)*(k-1))
icc=(msr-mse)/(msr+(k-1)*mse+k*(msc-mse)/nn)
# crude risk
r=st.pearsonr(df.forp_total,df.phq4)
conf=m.conf_int().loc['forp_per10'].tolist()
ns=int(complete.shape[0]);drop=n-ns
summary={
 'analysis_status':'SYNTHETIC / DEMONSTRATION ONLY', 'seed':SEED,'n_baseline':n,'n_followup_6m':ns,'dropouts_6m':drop,'followup_fraction':round(ns/n,3),
 'age_mean':round(age.mean(),1),'age_sd':round(age.std(ddof=1),1), 'female_n':int(female.sum()),'female_pct':round(female.mean()*100,1),
 'diagnosis_counts':df.diagnosis.value_counts().to_dict(),
 'forp_mean':round(forp.mean(),2),'forp_sd':round(forp.std(ddof=1),2),
 'who0_mean':round(who0.mean(),2),'who6_mean_observed':round(complete.who5_m6.mean(),2),
 'cronbach_alpha':round(alpha,3),'approx_omega_continuous':round(omega,3),'icc_absolute_agreement':round(icc,3),'n_retest':nn,
 'primary_beta_per10':round(float(m.params['forp_per10']),3),'primary_ci95':[round(float(x),3) for x in conf],
 'primary_p':float(m.pvalues['forp_per10']),'model_r2':round(float(m.rsquared),3),'model_base_r2':round(float(mb.rsquared),3),'delta_r2':round(float(m.rsquared-mb.rsquared),4),
 'interaction_beta':round(float(mi.params['forp_x_family']),3),'interaction_p':float(mi.pvalues['forp_x_family']),
 'clinical_n':int(complete.clinical_deterioration_m6.sum()),'clinical_rate':round(100*complete.clinical_deterioration_m6.mean(),1),
 'clinical_or_per10':round(float(np.exp(logit.params['forp_per10'])),3),
 'clinical_or_ci95':[round(float(np.exp(x)),3) for x in logit.conf_int().loc['forp_per10']],
 'clinical_p':float(logit.pvalues['forp_per10']),
 'cor_forp_phq':round(float(r.statistic),3),
 'restriction':'No human participants; hypothesis-driven generated variables; no ethics approval or real measurements.'}
(OUT/'results'/'summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
coefs=pd.DataFrame({'variable':m.params.index,'beta':m.params.values,'std_error':m.bse.values,'p':m.pvalues.values,'ci_low':m.conf_int()[0].values,'ci_high':m.conf_int()[1].values})
coefs.to_csv(OUT/'results'/'primary_regression.csv',index=False)
pd.DataFrame({'item':[f'FORP {i+1}' for i in range(10)],'factor_loading_continuous_ml':lambda_,'uniqueness':psi}).to_csv(OUT/'results'/'factor_loadings_continuous_approx.csv',index=False)

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.titlesize':15,'axes.spines.top':False,'axes.spines.right':False})
# 1 cohort
fig,ax=plt.subplots(figsize=(10,5.3));steps=[('Baseline',n),('Month 3',int(df.who5_m3.notna().sum())),('Month 6',ns),('Retest 28d',nn)];bars=ax.bar([x[0] for x in steps],[x[1] for x in steps],color=['#17567b','#327798','#5494ac','#84b2c2']);ax.set_ylim(0,415);ax.set_ylabel('Number of participants');ax.set_title('Cohort retention and reliability subsample');[ax.text(b.get_x()+b.get_width()/2,b.get_height()+8,str(int(b.get_height())),ha='center',fontsize=12,fontweight='bold') for b in bars];fig.tight_layout();fig.savefig(OUT/'figures'/'cohort_flow.png',dpi=170);plt.close(fig)
# 2 adjusted partial residual / model predicted trajectories for low vs high fear
fig,ax=plt.subplots(figsize=(10,5.3));temp=Xm.copy(); mid_fear=complete.forp_per10.median(); x=np.linspace(np.percentile(complete.forp_per10,5),np.percentile(complete.forp_per10,95),100); ref=Xm.mean(axis=0); preds=[]
for z in x:
    t=ref.copy();t['forp_per10']=z;preds.append(float(t @ m.params))
ax.scatter(complete.forp_total,complete.who5_m6,alpha=.20,s=16,color='#6c96ad',label='Individual observations')
ax.plot(x*10,preds,color='#b34e37',linewidth=3,label='Adjusted expected WHO-5')
ax.set(xlabel='Baseline FORP-MHQ total (0–40)',ylabel='WHO-5 at month 6 (0–100)',title='Prospective association, adjusted model')
ax.legend(frameon=False);fig.tight_layout();fig.savefig(OUT/'figures'/'prospective_association.png',dpi=170);plt.close(fig)
# 3 key effects
fig,ax=plt.subplots(figsize=(9.5,4.2)); v=['FORP-MHQ (per 10 points)','PHQ-4 (per point)','Family support (per point)','Stigma concern (per point)']; keys=['forp_per10','phq4','mspss_family_mean','stigma_concern'];ys=np.arange(4)[::-1]
for y,k in zip(ys,keys):
 lo,hi=m.conf_int().loc[k];ax.errorbar(m.params[k],y,xerr=[[m.params[k]-lo],[hi-m.params[k]]],fmt='o',capsize=4,color='#17567b',markersize=8)
ax.axvline(0,color='#444',alpha=.4);ax.set_yticks(ys,v);ax.set_xlabel('Adjusted difference in WHO-5 score (95% CI)');ax.set_title('Prespecified covariate estimates');fig.tight_layout();fig.savefig(OUT/'figures'/'forest.png',dpi=170);plt.close(fig)
# 4 construct distributions
fig,ax=plt.subplots(figsize=(10,4.9));ax.hist(df.forp_total,bins=np.arange(0,42,2),color='#286b8f',edgecolor='white');ax.set(xlabel='FORP-MHQ total',ylabel='Frequency',title='Distribution of baseline relapse fear');fig.tight_layout();fig.savefig(OUT/'figures'/'forp_distribution.png',dpi=170);plt.close(fig)
print(json.dumps(summary,ensure_ascii=False,indent=2))