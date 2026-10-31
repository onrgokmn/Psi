"""Transparent secondary descriptive and sensitivity analyses of simulated cohort."""
from pathlib import Path
import json
import numpy as np, pandas as pd
import scipy.stats as st
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
from matplotlib import pyplot as plt
DIR=Path(__file__).resolve().parents[1]
df=pd.read_csv(DIR/'data/synthetic_cohort.csv')
obs=df.who5_m6.notna();dc=df.loc[obs].copy()
Dc={}
Dc['n_base']=len(df);Dc['n_obs']=len(dc)
Dc['follow_up_3m']=int(df.who5_m3.notna().sum())
Dc['female_n']=int(df.sex_female.sum())
Dc['age_mean']=float(df.age.mean());Dc['age_sd']=float(df.age.std())
for c in ['forp_total','who5_baseline','who5_m3','who5_m6','phq4','mspss_family_mean','stigma_concern']:
 Dc[c]={'n':int(df[c].count()),'mean':round(float(df[c].mean()),2),'sd':round(float(df[c].std()),2),'median':round(float(df[c].median()),2),'q1':round(float(df[c].quantile(.25)),2),'q3':round(float(df[c].quantile(.75)),2)}
Dc['dx_counts']=df.diagnosis.value_counts().to_dict()
Dc['consequence_counts']=df.primary_feared_consequence.value_counts().to_dict()
Dc['medication_prescribed_n']=int(df.medication_prescribed.sum());Dc['mars_n']=int(df.mars5_total.count())
Dc['clinical_deterioration_n']=int(dc.clinical_deterioration_m6.sum())
Dc['attrition_by_dx']={k: {'recruited':len(s),'followed':int(s.who5_m6.notna().sum())} for k,s in df.groupby('diagnosis')}
Dc['attrition_diff']={k:round(float(df.loc[obs,k].mean()-df.loc[~obs,k].mean()),2) for k in ['age','forp_total','phq4','who5_baseline','mspss_family_mean']}
# regression controlled diagnostic reference alphabetic (Anxiety reference), replicates original generator
X=pd.concat([dc[['who5_baseline','phq4','age','sex_female','mspss_family_mean','stigma_concern']].astype(float),pd.get_dummies(dc.diagnosis,prefix='dx',drop_first=True,dtype=float)],axis=1)
X['forp_10']=dc.forp_total/10
X=sm.add_constant(X)
fit=sm.OLS(dc.who5_m6,X).fit(cov_type='HC3')
fit0=sm.OLS(dc.who5_m6,X.drop(columns='forp_10')).fit(cov_type='HC3')
Dc['regression']={'beta':round(float(fit.params['forp_10']),4),'CI':[round(float(z),4) for z in fit.conf_int().loc['forp_10']],'p':round(float(fit.pvalues['forp_10']),6),'r2':round(float(fit.rsquared),4),'delta_r2':round(float(fit.rsquared-fit0.rsquared),5),'n':int(fit.nobs)}
Dc['normality_y6_residual_test']= {'statistic':round(float(st.normaltest(fit.resid).statistic),3),'p':round(float(st.normaltest(fit.resid).pvalue),4)}
Dc['standardized_resid_max_abs']=round(float(np.abs((fit.resid-fit.resid.mean())/fit.resid.std(ddof=1)).max()),3)
Dc['max_vif']=round(float(max(variance_inflation_factor(X.to_numpy(),i) for i in range(1,X.shape[1]))),2)
Dc['spearman_forp_who6']=float(st.spearmanr(dc.forp_total,dc.who5_m6).statistic)
Dc['spearman_forp_phq4']=float(st.spearmanr(df.forp_total,df.phq4).statistic)
# Attrition weighting based only on baseline fields (IPW, normalization)
allx=pd.concat([df[['who5_baseline','phq4','age','sex_female','mspss_family_mean','stigma_concern','forp_total']].astype(float),pd.get_dummies(df.diagnosis,prefix='dx',drop_first=True,dtype=float)],axis=1)
allx=sm.add_constant(allx)
miss=sm.Logit(obs.astype(int),allx).fit(disp=False)
ps=miss.predict(allx);wt=np.clip(1/ps[obs],1,10)
ipw=sm.WLS(dc.who5_m6,X,weights=wt).fit(cov_type='HC3')
Dc['ipw']={'beta':round(float(ipw.params['forp_10']),3),'CI':[round(float(x),3) for x in ipw.conf_int().loc['forp_10']],'p':round(float(ipw.pvalues['forp_10']),4),'weight_min':round(float(wt.min()),3),'weight_max':round(float(wt.max()),3)}
# Pattern mixture scenarios: model-based expected outcome among missing plus explicit delta offsets
predx=allx.loc[~obs].copy(); predx=predx.drop(columns=['forp_total']);predx['forp_10']=df.loc[~obs,'forp_total']/10
predx=predx[X.columns]
for delta in [-15,-10,-5,0,5,10]:
 augmented=df.copy();augmentX=allx.drop(columns=['forp_total']);augmentX['forp_10']=df.forp_total/10;augmentX=augmentX[X.columns]
 yp=fit.predict(predx).to_numpy()+delta
 augmented.loc[~obs,'who5_m6']=np.clip(yp,0,100)
 fm=sm.OLS(augmented.who5_m6,augmentX).fit(cov_type='HC3')
 Dc.setdefault('delta_sensitivity',[]).append({'delta':delta,'beta':round(float(fm.params['forp_10']),3),'CI':[round(float(x),3) for x in fm.conf_int().loc['forp_10']]})
# report top means missing
for k,v in Dc.items():
 if isinstance(v,np.generic):Dc[k]=v.item()
(DIR/'results/expanded_summary.json').write_text(json.dumps(Dc,indent=2,ensure_ascii=False),encoding='utf-8')
# Table 1
summary=[]
for c,label in [('age','Age, years'),('forp_total','FORP-MHQ total'),('phq4','PHQ-4 total'),('who5_baseline','Baseline WHO-5'),('mspss_family_mean','Family support mean'),('stigma_concern','Disclosure concern (0-4)')]:
 for group,dd in [('All',df),('Followed',dc),('Lost',df.loc[~obs])]:
  summary.append({'variable':label,'group':group,'n':dd[c].notna().sum(),'mean':round(dd[c].mean(),2),'sd':round(dd[c].std(),2)})
pd.DataFrame(summary).to_csv(DIR/'results/table1_descriptive.csv',index=False)
pd.DataFrame({'term':fit.params.index,'beta':fit.params.values,'se_hc3':fit.bse.values,'p':fit.pvalues.values,'ci_low':fit.conf_int()[0].values,'ci_high':fit.conf_int()[1].values}).to_csv(DIR/'results/table2_adjusted_regression.csv',index=False)
# Attrition bar
fig, ax=plt.subplots(figsize=(9,4.5),dpi=160)
labels=list(Dc['attrition_by_dx']); rates=[100*Dc['attrition_by_dx'][k]['followed']/Dc['attrition_by_dx'][k]['recruited'] for k in labels]
ax.bar(labels,rates,color='#17617a');ax.set_ylim(0,100);ax.set_ylabel('Six-month follow-up (%)');ax.set_title('Follow-up completeness by diagnosis',loc='left',fontweight='bold')
for i,x in enumerate(rates):ax.text(i,x+1,f'{x:.0f}%',ha='center',fontsize=9)
ax.spines[['top','right']].set_visible(False);fig.tight_layout();fig.savefig(DIR/'figures/attrition_by_diagnosis.png',bbox_inches='tight');plt.close(fig)
print(json.dumps(Dc,indent=2,ensure_ascii=False))