# FORP-TR / V4.0 · Preregisterable clinical research protocol

**Status: Planned, not conducted.** No real participant data have been collected and no ethics approval or Turkish FORP-MHQ validity is asserted. Earlier V3 generated cohort data remain a separate computational demonstration, not clinical results.

## Key fixed decisions

- **Single primary hypothesis:** Baseline FORP-MHQ total/10 is conditionally associated with six-month WHO-5, adjusting for baseline WHO-5, PHQ-4, age, sex, diagnostic family and episode burden.
- **N=500 at baseline**, assuming 20% attrition → 400 month-six outcomes. For *partial R²=0.02*, power ≈81.3%; for 0.01, ≈51.8% (two-sided alpha=0.05, 10 planned slopes; noncentral-F approximation).
- **Patient burden:** 25 responses at baseline (10 FORP, 5 WHO-5, 4 PHQ-4, 4 MSPSS family, 2 context); five WHO-5 questions at months three and six.
- **Cultural substudy:** 24–30 purposively selected interviews distributed among high/low FORP × high/low family support, analysed by framework analysis and integrated through a joint display.

## Documents

- `protocol/Nihai_protokol_SAP_TR.md` (+ DOCX/PDF): main ethics-ready study protocol and statistical analysis plan.
- `thesis/Tez_proje_metni_V4.md` (+ DOCX/PDF): updated Turkish specialist thesis **proposal** (not completed results).
- `manuscript/Prospective_protocol_EN.md` (+ DOCX/PDF): English protocol article with structured abstract and pre-defined reporting framework.
- `forms/Hasta_uygulama_formu_TR.md` (+ DOCX/PDF): short form skeleton, without copyrighted or unapproved translated items.
- `qualitative/Kulturlerarasi_gorusme_ve_joint_display.md` (+ DOCX/PDF): actual clinical interview prompts, matrix and integration plan.
- `analysis/power_calculator.py`, `power_scenarios.csv`, `power_summary.json`: independently executable sample size sensitivity.
- `figures/power_curve.png`: power curve plotting example.
- `slides/Nihai_tez_protokolu_V4.pptx` (+ PDF): 18-slide editable defense.

## Execution gates

1. Verify FORP Turkish novelty and obtain written permission.
2. Obtain institutional and ethics approvals, confirm permitted translations.
3. Conduct 15–20 cognitive interviews and 25–40 patient pilot, lock Turkish wording.
4. Register protocol before recruitment; feasibility check without outcome association access.
5. Recruit consecutively, monitor attrition, and report STROBE/COSMIN/COREQ transparently.

**Recommended source:** Coutts-Bain et al. 2025 doi:10.1111/bjc.12536; Gagnier et al. 2025 doi:10.1007/s11136-025-03950-x; Tong et al. 2007 doi:10.1093/intqhc/mzm042.