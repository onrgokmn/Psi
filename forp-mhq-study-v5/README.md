# FORP-TR V5 · Major Revision: preregisterable prospective psychiatry protocol

**Version:** 5.0 (31 October 2026). **Status:** Proposed research design, **not an approved or conducted clinical study**. No results of simulated participants appear as clinical findings.

## What changed since V4

1. All previously generated cohort effects were removed from the main clinical text; Monte Carlo **design only** now lives in `appendices/Ek_A_Monte_Carlo.md`, with a reproducible script.
2. Monte Carlo sample sizing includes predeclared confounders, HC3 robust regression, observed-score boundaries, 20% attrition and MAR/MCAR/MNAR sensitivity. N=700 is recommended for the specified effect; subgroups are exploratory.
3. PHQ-4 is replaced by PHQ-9 + GAD-7. Illness duration, episodes, baseline treatment, clinical remission, and centre if applicable are required baseline covariates.
4. Translation/pilot is separate from main cohort: none of its participants enters the primary clinical analysis; outcome-blinded baseline psychometrics follows.
5. Restricted cubic spline nonlinearity with 3 prespecified knots is secondary, no data-driven cut-off.
6. Diagnosis-specific clinical episodes have two blinded clinician ratings and third-adjudicator disagreement resolution; WHO-5 is not relapse.
7. A fully populated *draft* OSF preregistration plus STROBE/COSMIN 2.0 crosswalk is ready. **OSF submission has not occurred.**
8. Formal language, consistent terminology and refined document layout in Turkish and English.

## Key files

- `protocol/FORP_TR_V5_Nihai_Protokol_ve_SAP.md` · Turkish full protocol and SAP.
- `thesis/Tez_Onerisi_V5.md` · revised thesis proposal.
- `manuscript/FORP_V5_Prospective_Protocol_EN.md` · international-journal structured protocol.
- `appendices/Ek_A_Monte_Carlo.md` · only location for simulations and hypothetical data-generating assumptions.
- `analysis/monte_carlo_power.py` · reproducible power experiment; seed 20261031.
- `checklists/STROBE_COSMIN_Uyum_Matrisi.md` · reporting audit against original official checklists.
- `registration/OSF_ON_KAYIT_TASLAGI.md` · OSF registration-ready content, not registered.
- `forms/Kisa_Hasta_Formu_V5.md` · 37 baseline patient responses; five at follow-up.
- `forms/Nuks_Kor_Degerlendirme_El_Kitabi.md` · blinded diagnosis-specific endpoint definitions.

**Scientific limitations:** Selected partial R² and generated covariate distributions are assumptions, not empirical estimates; model sensitivity to MNAR remains substantial. Translation permission, ethics/site approval, OSF registration and real participant data are mandatory before clinical inference.