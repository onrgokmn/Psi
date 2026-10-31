# FORP-TR: single-centre psychometric thesis protocol (V9)
**Status:** planning document, not completed human research. Full editable DOCX/PDF package and executable analysis sources were delivered in the associated ChatGPT conversation as `FORP_TR_V9_TEK_MERKEZ_PSIKOMETRI_TEZ.zip`.

## Scope
- Thesis: Turkish cross-cultural adaptation and psychometric evaluation of the ten-item FORP-MHQ in adults with depressive or anxiety disorders.
- Target: 300 fully observed questionnaires, 250 strictly conditional lower bound **not approved** before ordinal CFA simulation.
- One centre, 20-month core schedule (24-month buffer), ≥7 analysable records/week target.
- Separate iterative cognitive pilot, 5–10 participants per round.
- WLSMV 1-factor CFA, ordinal omega, I-CVI, prespecified correlations and known-group validity; retest 14±3 days in clinically stable subset.
- No prospective relapse cohort, adjudication, or mixed-methods study is part of the thesis.

## Verification boundary
A 1,000-replicate-per-scenario Python simulation assessed ordinal response cell sparsity. It was not a WLSMV power simulation. Full R/lavaan simulation code is included in the full package but **has not been executed** in this runtime. Authors must run it and preregister the final N rationale before ethics-approved recruitment.

## Ethics
Authorship, author permission for the translated scale, ethics approval, clinician-led suicide-risk SOP, independent consent workflow, and KVKK processing authorization are pending. No translated copyrighted items or patient records are public.

## Corrections from prior reviews
Correct title and sample frame; omit internal reviewer language from the thesis; prespecified 300 target and 250 conditional floor; explicit exclusion rules; diagnosis-specific clinician classification; transparent construct-validity hypotheses; conditional invariance; conservative interpretation of WLSMV fit indices; local-dependence and loading rules; exploratory EFA/GRM fallback; full bibliographic references, code and figures in deliverable archive.
