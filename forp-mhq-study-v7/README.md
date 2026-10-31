# FORP-TR V7 | Major reviewer revision (31 October 2026)
**Status:** Preregistration-ready methodological DRAFT only. No patients recruited, no ethics approval, no FORP-MHQ Turkish authorization, and no OSF registration.

## Controlling protocol
The V7 protocol now uses a single confirmatory estimand: six-month WHO-5 point difference per 10 baseline FORP-MHQ points (beta_1), adjusted for 12 prespecified baseline degrees of freedom. Clinical outcome analyses are gated by prospective Turkish measurement evaluation.
- Primary groups: depressive and anxiety disorders (not psychotic/bipolar/OCD).
- Independent linguistic pilot (30-40); first 250 cohort baselines undergo blinded psychometric gate before outcome analysis. Green/amber/red decisions predefine whether confirmatory inference proceeds.
- Prespecified exploratory nonlinearity: 3-knot spline; not independently powered.
- Clinical worsening adjudication masked to FORP and fear-related prose.
- Outpatient suicide-risk SOP includes immediate assessment when warranted, safe deferred form completion, secure contacts, after-hours protocol.
- Two centres are required for a feasible 700-recruit target, but the second centre is NOT approved.
- All text and source-code deliverables are contained in the separately created full V7 research package. Nothing here is a completed clinical study.

### Monte Carlo planning
1,000 synthetic simulations/scenario; seed 20261031; N=700 baseline, n~560 observed T6; 14-parameter full covariate design; two-sided alpha 0.05, HC3 complete-case OLS (NOT 40-fold MICE).
Partial R2 .015, residual SD14: 82.1% power (MCSE 1.21 percentage points), beta=-2.219 WHO-5 points/10 FORP. Sensitivity SD16: 71.6%; SD18: 56.7%. Partial R2 .01 and SD14: 64.0%. At N=900/720, SD16, effect fixed: 81.1%.
The assumed partial R2 is a STATISTICAL planning SESOI candidate, NOT a clinically validated effect size or WHO-5 MCID.
The R MICE plan is not yet independently validated by an identical Monte Carlo simulation.

### Open issues before ethics application
Original-scale author written permission, confirmed second site/staffing, clinician-approved emergency SOP, data processing terms, institutional retention periods and blinded analysis freeze.
