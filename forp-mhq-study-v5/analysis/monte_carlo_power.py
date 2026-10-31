#!/usr/bin/env python3
"""FORP-TR V5 pre-recruitment MONTE CARLO power laboratory.
SIMULATION ONLY. No participant outcomes or empirical clinical claims.
Reproducible seed; HC3 inference; predeclared baseline covariates; MAR attrition.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
import numpy as np, pandas as pd
from scipy.special import expit
from scipy.stats import t as student_t
import json
from pathlib import Path

OUT=Path(__file__).resolve().parents[1]/'analysis'; OUT.mkdir(parents=True,exist_ok=True)
SEED=20261031
REPS=int(os.environ.get('MC_REPS','500'))
SIGMA=14.0
NGRID=[400,500,600,700,850,1000]
P_R2=[0.0,0.01,0.02]

# Prospective covariates drawn from plausible scenarios, NOT measured Balikesir distributions.
def make_x(n,rng):
    age=np.clip(rng.normal(44,14,n),18,85)
    sex=rng.binomial(1,.56,n)
    diagnosis=rng.choice(4,n,p=[.37,.34,.18,.11]); diag=np.column_stack([(diagnosis==v).astype(float) for v in (1,2,3)])
    duration=np.exp(np.clip(rng.normal(1.32,.85,n),-1.5,3.8))
    epi_raw=rng.poisson(np.maximum(.2,.25+duration*.19))
    episode=np.clip(epi_raw,0,2).astype(float)
    remission=rng.binomial(1,expit(.45-.15*(episode>=2)-.35*(diagnosis==2)))
    treatment=rng.choice(3,n,p=[.16,.59,.25]); tx=np.column_stack([(treatment==v).astype(float) for v in (1,2)])
    phq=np.clip(np.round(rng.normal(9.5+2.4*(1-remission)+1.0*(diagnosis==0),4.9,n)),0,27)
    gad=np.clip(np.round(rng.normal(7.5+.26*phq+1.0*(diagnosis==1),4.2,n)),0,21)
    who=np.clip(np.round((68-1.45*phq-.55*gad+4*remission+rng.normal(0,12,n))/4)*4,0,100)
    forp=np.clip(np.round(10+.65*phq+.37*gad+1.2*episode-3*remission+rng.normal(0,7,n)),0,40)
    x=forp/10.0
    # 14 predeclared adjusters (intercept excluded): WHO5, PHQ-9, GAD-7, age, sex, diagnosis(3),
    # log duration, prior episodes, treatment(2), remission. 13 covariates total.
    base=np.column_stack([np.ones(n),who,phq,gad,(age-45)/10,sex,diag,np.log1p(duration),episode,tx,remission])
    return x,base,np.column_stack([who,phq,gad,remission,episode])

def residual_var(x,b):
    c=np.linalg.lstsq(b,x,rcond=None)[0]
    z=x-b@c
    return float(z@z/len(z))

def calibrate_beta(partial_r2,rng):
    if partial_r2==0:return 0.0
    x,b,_=make_x(100000,rng)
    varx=residual_var(x,b)
    return -float(np.sqrt((partial_r2/(1-partial_r2))*SIGMA**2/varx))

# Logistic intercept calibrated to 20% expected missing outcomes, conditional on observed T0.
def observation_prob(a):
    lo,hi=-10.0,10.0
    for _ in range(28):
        mid=(lo+hi)*.5
        if expit(mid+a).mean()>.8:hi=mid
        else:lo=mid
    return expit((lo+hi)/2+a)

def fit(y,b,x,keep):
    mm=keep & np.isfinite(y)
    m=int(mm.sum());a=np.column_stack([b,x])[mm]; yy=y[mm];p=a.shape[1]
    if m<=p+8:return np.nan,np.nan,np.nan,m
    try:
        coef=np.linalg.lstsq(a,yy,rcond=None)[0]
        inv=np.linalg.pinv(a.T@a)
        e=yy-a@coef
        leverage=np.einsum('ij,jk,ik->i',a,inv,a)
        scal=(e/np.maximum(1-leverage,1e-6))**2
        vcov=inv@((a*scal[:,None]).T@a)@inv
        se=np.sqrt(max(vcov[-1,-1],1e-15))
        stat=coef[-1]/se
        pval=2*student_t.sf(abs(stat),df=m-p)
        return float(coef[-1]),float(se),float(pval),m
    except np.linalg.LinAlgError:return np.nan,np.nan,np.nan,m

def one_sim(n,beta,rng,mode='MAR'):
    x,b,ctx=make_x(n,rng)
    who,phq,gad,rem,episodes=ctx.T
    # Explicit DGP (for power planning), including baseline symptoms and confounder effects.
    eps=rng.normal(0,SIGMA,n)
    latent=32+.48*who-.24*phq-.11*gad+2.2*rem-.55*episodes+beta*x+eps
    # WHO-5 has a bounded 0..100 scale and score steps of 4.
    y=np.clip(np.round(latent/4)*4,0,100)
    a=-.052*(x*10-20)+.018*(who-50)-.027*(phq-10)+.22*rem
    if mode=='MCAR':a=np.zeros(n)
    if mode=='MNAR':a=a+.060*(y-50) # more loss in individuals with lower unobserved well-being
    probs=observation_prob(a)
    observed=rng.uniform(size=n)<probs
    est,se,p,nobs=fit(y,b,x,observed)
    return est,se,p,nobs/n,probs.mean()

def run():
    rng=np.random.default_rng(SEED)
    betas={v:calibrate_beta(v,rng) for v in P_R2}
    rows=[]
    for n in NGRID:
        for effect in P_R2:
            data=np.array([one_sim(n,betas[effect],rng,'MAR') for i in range(REPS)])
            est,se,p,rate,prob=data.T
            p=p[np.isfinite(p)]; est=est[np.isfinite(est)];se=se[np.isfinite(se)]
            power=float(np.mean(p<.05))
            # Monte Carlo SE is binomial accuracy of estimated power, not uncertainty in true clinical effect
            mcse=float(np.sqrt(power*(1-power)/len(p)))
            rows.append(dict(recruited=n,completed_mean=round(n*float(rate.mean()),1),partial_r2_target=effect,assumed_beta_per10=round(betas[effect],3),missingness='MAR',replicates=len(p),empirical_power=round(power,4),mc_se=round(mcse,4),power_ci_low=round(max(0,power-1.96*mcse),4),power_ci_high=round(min(1,power+1.96*mcse),4),mean_observed_pct=round(float(rate.mean())*100,1),mean_slope=round(float(np.mean(est)),3),mean_hc3_se=round(float(np.mean(se)),3),coverage=round(float(np.mean((est-1.96*se<=betas[effect])&(est+1.96*se>=betas[effect]))),4)))
        print(f'MAR N={n} complete',flush=True)
    # planned robustness analysis under non-ignorable missingness at the selected N
    for n in [600,700,850]:
        for mode in ['MCAR','MNAR']:
            for effect in [0.,.02]:
                data=np.array([one_sim(n,betas[effect],rng,mode) for _ in range(REPS)])
                est,se,p,rate,prob=data.T
                power=np.nanmean(p<.05);mcse=np.sqrt(power*(1-power)/REPS)
                rows.append(dict(recruited=n,completed_mean=round(n*float(rate.mean()),1),partial_r2_target=effect,assumed_beta_per10=round(betas[effect],3),missingness=mode,replicates=REPS,empirical_power=round(float(power),4),mc_se=round(float(mcse),4),power_ci_low=round(float(max(0,power-1.96*mcse)),4),power_ci_high=round(float(min(1,power+1.96*mcse)),4),mean_observed_pct=round(float(rate.mean())*100,1),mean_slope=round(float(np.mean(est)),3),mean_hc3_se=round(float(np.mean(se)),3),coverage=round(float(np.mean((est-1.96*se<=betas[effect])&(est+1.96*se>=betas[effect]))),4)))
    tab=pd.DataFrame(rows)
    tab.to_csv(OUT/'monte_carlo_results.csv',index=False)
    meta={'seed':SEED,'replicates_per_scenario':REPS,'target_partial_r2':P_R2,'effect_betas_per10':{str(k):v for k,v in betas.items()},'analysis':'HC3 OLS, complete outcome, all 13 baseline adjustment terms','alpha':.05,'target_followup_rate':.8,'sample_grid':NGRID,'clinical_participant_data':'none', 'interpretation':'Only Monte Carlo design sensitivity; power is not an observed study outcome.'}
    (OUT/'monte_carlo_metadata.json').write_text(json.dumps(meta,indent=2,ensure_ascii=False),encoding='utf8')
    print(tab.to_string(index=False)); print(json.dumps(meta,indent=2))

if __name__=='__main__':run()