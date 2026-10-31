# FORP-TR · V5 Peer-review revision (31 October 2026)

**Status: proposed clinical study. No recruitment, ethics approval, OSF registration or empirical results.**

## Prespecified clinical question
Does baseline fear of recurrence (FORP-MHQ; per 10 score points) show an adjusted association with WHO-5 psychological well-being at 6 months among adult psychiatric outpatients?

## Eight material changes
1. Simulated cohort effects have been removed from clinical abstract/results/discussion; methods-only Monte Carlo planning is in Appendix A.
2. Monte Carlo planning (500 replications/scenario; seed 20261031; N=400–1000; partial R²=0/.01/.02; MCAR/MAR/MNAR). N=700 gives ~89.6% power if partial R²=.02 and 20% attrition; for .01, ~58.4%. This is conditional, not observed evidence.
3. Primary model adjusts for baseline WHO-5, PHQ-9, GAD-7, age, sex, diagnosis family, log illness duration, prior episode burden, baseline treatment category, baseline remission and site if applicable.
4. Adaptation/cognitive debriefing/pilot are separate from primary cohort participants. Translation authorization remains pending.
5. Restricted cubic spline (baseline FORP 10th/50th/90th percentiles) prespecified as secondary nonlinearity analysis; U-shaped inference cannot be based on a spline p value alone.
6. Diagnosis-specific new episodes and active-disease worsening are separate secondary endpoints, adjudicated by two psychiatrists blinded to baseline FORP and cultural responses.
7. Prepared OSF registration text and STROBE/COSMIN/COREQ reporting crosswalk; OSF has NOT been submitted.
8. Professional Turkish thesis proposal, English prospective protocol, patient forms and presentation, with academic language and clearly scoped limitations.

## Key design
- 700 enrolled, ~560 completing month 6 (assumed 20% loss)
- 37 patient item responses at baseline, 5 WHO-5 items at months 3/6
- 15–20 cognitive interviews and 30–40 pilot participants separately
- 70–90 retest volunteers; 24–30 explanatory cultural interviews
- Primary HC3 robust linear regression; multiple-imputation/IPW/MNAR sensitivity
- Diagnosis-specific clinical event criteria and blinded review

**Full dated research bundle:** Download the V5 ZIP supplied in the ChatGPT conversation. This GitHub directory initially contains the protocol summary, preregistration outline and methodological assumptions; the ZIP holds complete editable DOCX, PDFs, Python, R, data-free scripts and slides. No individual patient data are or should be published in GitHub.

Scientific sources:
- https://doi.org/10.1111/bjc.12536
- https://doi.org/10.1007/s11136-025-03950-x
- https://www.strobe-statement.org/checklists/
- https://help.osf.io/article/330-welcome-to-registrations
