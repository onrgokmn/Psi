# FORP-TR V4: Preregistered Primary Analysis — Implementation Specification
**Status: future study protocol, NOT observed patient outcomes.** Full Word/PDF/PowerPoint research package was generated separately in the current chat.
## Single confirmatory research question
Among adults receiving outpatient psychiatric care, is baseline fear of mental-illness recurrence/progression (FORP-MHQ total, 0–40) conditionally associated with subjective well-being at six months (WHO-5, 0–100), beyond baseline well-being, PHQ-4, age, sex, four-category diagnostic family and prior episode burden?
**Estimand:** Mean six-month WHO-5 point difference per 10 points of baseline FORP, adjusting for the fixed baseline covariates. Not a causal treatment effect, not a prediction of clinical relapse, and not a clinical cutoff.
## Target study and sample-size rationale
Baseline N = 500. With an assumed 20% attrition, expected completed outcome N = 400.
For a single extra slope coefficient, approximately 10 total model coefficients, two-sided alpha=.05, incremental *partial* R²=.02, a noncentral F calculation requires n≈387 completed participants for 80% power. N=400 provides ≈81.3% power for partial R²=.02 but only ≈51.8% for .01. Approximation assumes ordinary linear-model information and is sensitive to attrition, model complexity and center clustering. DO NOT confuse partial R² with raw ΔR².
Site feasibility assessed using *recruitment and consent rates only*, before reviewing outcome associations. Add a second site with a protocol amendment if single-site recruitment is infeasible.
## Baseline patient burden: fixed 25-item battery
- FORP-MHQ: 10 items, one-month reference, permission and translation REQUIRED
- WHO-5: 5 items, prior two weeks, score (0–25)*4
- PHQ-4: 4 items, prior two weeks; verify Turkish license/translation
- MSPSS Family: 4 items; verify Turkish subscale stand-alone use/permissions
- Two investigator-created descriptive context questions: most-feared consequence; concern about illness/treatment disclosure. THESE ARE NOT A VALIDATED STIGMA SCALE.
At months 3 and 6 patients complete WHO-5 only (5 items). In a stable n=60–80 subgroup, FORP-MHQ retest at 28 days.
## Measurement-property preconditions
Written permission, translation reconciliation, blinded back translation, expert review, 15–20 cognitive debriefing interviews, 25–40-person pilot, form freeze; ordinal CFA for single-factor ten-item model (WLSMV); thresholds and standardized loadings; omega/alpha with CIs; stable-subgroup absolute-agreement ICC. No modification-index fishing or invented Turkish validation.
## Primary statistical model
WHO5_month6 = intercept + b1*(FORP_baseline/10) + b2*WHO5_baseline + b3*PHQ4_baseline + b4*age + b5*sex + 3 diagnostic indicators + episode-burden score + error.
Main estimator: OLS with HC3 robust uncertainty; report n, b1 (95% CI), two-sided p, reduced/full R², ΔR², partial R², model assumptions. No stepwise covariate selection. Explore nonlinearity and exposure interactions as labelled sensitivity/exploratory analyses.
For missing six-month WHO-5, report follow-up patterns, standardized baseline differences, MAR multiple imputation / inverse probability weighting, and prespecified MNAR pattern-mixture shifts. Do not attach fake CIs to single imputation.
## Cultural substudy
Purposive 24–30 interviews in the four combinations of high/low FORP × high/low MSPSS family support (~6–8 each), diversifying age, sex, diagnosis, education and rural/urban background. Examine family help vs control, privacy/stigma concerns, independence, avoidance, productive fear and contradictory stories. Framework analysis; triangulate quantitatively with a joint display. NO simulated quotations or essentialist generalizations.
## Execution & publication gates
Check FORP Turkish novelty, obtain written license and hospital/ethics approvals, register protocol and analysis plan before patients, verify survey timing, ensure secure coded health data never stored on public GitHub.
Cohort reporting: STROBE; measurement reporting: COSMIN 2.0; interviews: COREQ.
## Key research sources
- Coutts-Bain D, Sharpe L, Hunt C. *Br J Clin Psychol*. 2025. https://doi.org/10.1111/bjc.12536
- Gagnier JJ et al. *Qual Life Res*. 2025. https://doi.org/10.1007/s11136-025-03950-x
- WHO. WHO-5. https://www.who.int/publications/m/item/WHO-UCN-MSD-MHE-2024.01
- Tong A et al. *Int J Qual Health Care*. 2007. https://doi.org/10.1093/intqhc/mzm042
- Fetters MD et al. *Health Serv Res*. 2013. https://doi.org/10.1111/1475-6773.12117
