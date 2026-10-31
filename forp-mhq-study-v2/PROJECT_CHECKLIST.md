# Final research-compliance checklist

**Status:** computational simulation and draft research protocol, not a completed human-subjects investigation.

## Prerequisites for any real-world ethics submission

1. Establish permission from the copyright holder to translate, reproduce, and use FORP-MHQ. Permission to access the published paper is not synonymous with a validated translation license.
2. Search PubMed, TR Dizin, TOAD, YÖK Tez Merkezi and clinical-trial registries again for completed/ongoing Turkish adaptations.
3. Confirm institution-appropriate thesis template, exact departmental attribution, supervisory approvals and ethics board jurisdiction.
4. Prepare a recruitment log recording invited, eligible, declined, excluded, consented, and follow-up status, without exposing psychiatric patient identities.
5. Obtain written consent for baseline/follow-up and separate permission for interview recording. Protect appointment reminders from disclosing diagnoses.
6. Execute forward-translation, reconciled versions, independent back-translation, expert panel, cognitive debriefing, and pilot time burden assessment.
7. Specify primary estimand, outcome handling, effect size and event-rate assumptions before empirical power calculations. Avoid claiming N=360 is proven adequate for interactions or multigroup invariance.
8. Add a priori definition of clinically stable participants for ICC, diagnosis-specific episode adjudication, detailed treatment and remission status, and recruitment strategy.
9. Document exact published Turkish versions and authorized administration of PHQ-4, WHO-5, MSPSS family items and any treatment-adherence tool.
10. Specify missing data diagnostics, residual diagnostics, ordered-item WLSMV CFA, internal consistency with CIs, ICC specification, and sensitivity strategies before looking at outcomes.
11. Register analysis plan before actual data collection where feasible. Use STROBE, COSMIN 2.0, COREQ for the respective components.
12. Do not publish generated values or present them to a committee as clinical observations. Replace only after valid recruitment and analyses, with complete research disclosure.

## Explicitly not yet demonstrated
- Turkish FORP-MHQ psychometric validity; measurement invariance; causal effects; recurrence of disease; cultural determinants; comparative efficacy; an observed clinical trajectory.
- Participant interviews, real treatment adherence responses, IRB approval, financial disclosures or actual author contributions.

## Results files and formulas
The robust linear model, follow-up observation weighting, and scenario sensitivity are described in the manuscript Methods and calculated in scripts/expanded_analysis.py. The synthetic generator places a negative direct FORP term into the 6-month WHO-5 outcome; the estimated coefficient cannot be treated as an independent discovery.