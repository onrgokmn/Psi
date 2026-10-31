#!/usr/bin/env python3
"""FORP-TR V4 power sensitivity: planning only, no patient data.
Runs with scipy: python power_calculator.py
"""
from scipy.stats import ncf, f
from scipy.optimize import brentq
import csv
PREDICTORS=10
def statistical_power(n,partial_r2,alpha=0.05,predictors=PREDICTORS):
    df=n-predictors-1
    threshold=f.ppf(1-alpha,1,df)
    f2=partial_r2/(1-partial_r2)
    return float(ncf.sf(threshold,1,df,n*f2))
def n_required(partial_r2,power_target=.8):
    return next(n for n in range(PREDICTORS+10,20001) if statistical_power(n,partial_r2)>=power_target)
def detectable_partial_r2(n,power_target=.8):
    return brentq(lambda pr2:statistical_power(n,pr2)-power_target,1e-6,.25)
if __name__=="__main__":
    print("partial R² required completed N:",[(r,n_required(r)) for r in [0.01,0.02,0.03]])
    print("N=400 power",[(r,statistical_power(400,r)) for r in [.01,.02,.03]])
    print("N=400 minimum detectable partial R²",detectable_partial_r2(400))
    with open("power_scenarios.csv","w",newline="") as fp:
        writer=csv.writer(fp);writer.writerow(["baseline_N","attrition","complete_N","power_R2_0.01","power_R2_0.02","power_R2_0.03"])
        for baseline in [350,400,420,450,480,500,550,600]:
            for attrition in [.15,.2,.25]:
                n=round(baseline*(1-attrition))
                writer.writerow([baseline,attrition,n,*[round(statistical_power(n,r),3) for r in [.01,.02,.03]]])
