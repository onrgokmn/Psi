# When Fear of Relapse Becomes Burdensome: Cultural Context, Family Support, and Six-Month Well-Being in a Transdiagnostic Mental Health Cohort

**RESEARCH DEMONSTRATION: simulated participants and modeled outcomes, not clinical observations. Not suitable as evidence of efficacy, validity or clinical prediction.**

**Manuscript type:** Methodological demonstration / simulated prospective cohort. **Target format:** structured abstract, introduction, methods, results, discussion, limitations, references, tables and figures. **Authors:** [to be determined upon actual study]. **Institution:** [to be confirmed]. **Ethics:** no human participants in this demonstrator; no real IRB approval claimed.



## Structured abstract

**Background.** Fear of recurrence and progression (FORP) is a transdiagnostic concern that may contribute to maladaptive vigilance, relationship restriction and altered treatment behavior. Whether FORP adds prospective information beyond baseline symptoms remains uncertain.

**Methods.** A hypothesis-driven dataset representing 360 hypothetical psychiatric outpatients was generated using a fixed random seed. The study specification included the 10-item FORP-MHQ, PHQ-4, WHO-5, perceived family support and a single-item stigma concern indicator. The primary analysis used six-month WHO-5 as outcome with baseline WHO-5, FORP, PHQ-4, family support, age, sex, stigma and diagnosis as covariates; HC3 robust standard errors were used. All observations and outcomes were generated in software.

**Results.** Among 303 records with observed six-month outcomes, the adjusted difference in six-month WHO-5 per 10 FORP points was -2.13 (95% CI -3.97 to -0.30, p=0.023); incremental R² was 0.011. FORP alpha was 0.948 and absolute-agreement test–retest ICC was 0.954 in 65 selected synthetic records. This is a computational exercise, not empirical validation.

**Conclusions.** This demonstrator specifies a low-burden prospective protocol suitable for real-world testing. It does not establish the Turkish form's validity, prognostic utility, or culture-specific pathways.

## Introduction

Recurrence and progression fears are clinically salient among people with mental health conditions even during periods of symptomatic improvement. A 2023 mixed-methods synthesis identified quality-of-life, anxiety, depression and medication adherence associations, along with a low-risk/low-reward lifestyle, hypervigilance and constrained life goals [2]. The 2025 FORP-MHQ development study presented a 10-item single-factor transdiagnostic measure in 865 participants [1]. A subsequent transdiagnostic investigation highlighted reassurance seeking, avoidance, shame and intrusive thoughts [3]. These observations motivate prospective work but do not prove that relapse fear causes subsequent impairment.

Cross-cultural adaptation is not merely linguistic translation. In the Turkish clinical setting, perceived family support and fear of social disclosure may be relevant contextual exposures. The perceived family support dimension of the MSPSS has Turkish psychometric evidence [4]. Cultural heterogeneity demands direct measurement rather than assumptions about patients' beliefs, family structures, or religiosity. Broad diagnostic eligibility can improve feasibility in a single-center outpatient setting but introduces case-mix heterogeneity requiring transparent reporting.

The proposed clinical question is whether baseline relapse fear predicts later psychological well-being independently of initial symptom load, and whether perceived family support modifies this association. An auxiliary qualitative component would explore when relapse fear promotes appropriate care and when it constrains relationships or meaningful activity. The present computational demonstrator evaluates the operational pipeline only.

## Methods

### Design and setting

Design specified: prospective single-center mixed-methods cohort with three waves (baseline, three months, six months), a 28-day retest subset, and cognitive interviews for Turkish cultural adaptation. The **executed component** is an artificial cohort generated in Python; no clinic, appointment or human participant was involved. Hence this manuscript must not be submitted as an empirical investigation.

### Participants, eligibility, and selection

For future implementation: sequential adults (≥18 years) attending psychiatry outpatient services with prior mental health condition experience and capacity to give informed consent. Patients unable to understand items due to severe acute disorganization or delirium would be excluded according to a prespecified clinical rule. Diagnostic groups should be reported and eligibility logged. The present generator produced 360 independent pseudonymous records with diagnoses randomly assigned among depression, anxiety, bipolar disorder, OCD, and other.

### Cultural adaptation and cognitive interviewing

Obtain written permission for translation, research and publication from scale rightsholders before use. Conduct two independent forward translations, reconciliation, blinded back-translations, expert review, cognitive debriefing interviews across educational and diagnostic groups, and pilot testing. Do not represent the ten item codes in this demonstrator as an authorized Turkish translation. For cultural context, elicit patients' perceived consequences of recurrence (symptoms, family, work, stigma, autonomy, other) and a direct concern about others learning about mental health treatment; these are exploratory variables, not a validated cultural scale. Include voluntary interviews with purposive diversity until thematic information power is reached. Follow ITC and COSMIN principles [5,7].

### Assessment schedule and participant burden

Baseline: FORP-MHQ 10 items (subject to permission), PHQ-4 four items, WHO-5 five items, MSPSS family subscale four items, optional medication adherence five items for medicated patients, and two cultural-context questions. The expected burden of 7–10 minutes requires real pilot timing. At three months use WHO-5 alone; at six months use WHO-5 plus medication adherence for medicated patients, together with a structured clinician adverse-course form from records. The dataset generator includes a 28-day retest score. In real use, clinically meaningful episode recurrence must be defined a priori using standardized diagnosis-specific criteria; symptom persistence is not necessarily recurrence.

### Primary outcome and hypotheses

The primary endpoint is continuous WHO-5 at six months (0–100) with baseline WHO-5 adjustment. The main exposure is FORP-MHQ total (0–40), reported per 10-point increase. The primary hypothesis is a negative adjusted association. Secondary outcomes: clinician-verified deterioration, medication adherence and explanatory qualitative themes. Family-support interaction and stigma-context analyses are explicitly exploratory, and their interpretation must avoid causal claims.

### Synthetic data generation

Seed = 20261031; baseline N=360. Underlying Gaussian variables generated ordinal FORP, PHQ-4 and family support item scores; a linear data-generating model created WHO-5 baseline and month-six outcome with a designed negative FORP parameter. Stigma influenced both fear and later well-being; follow-up dropout probability was associated with symptom and FORP levels. Thus the test can demonstrate a statistically significant model by construction and is **not** external validation. All randomization and calculations are reproducible with `scripts/generate_and_analyze.py`.

### Statistical plan

Analyses were specified in advance of reading the generated output: (1) descriptive summaries and missingness; (2) ten-item Cronbach alpha; (3) one-factor approximate omega from standardized item covariance using continuous maximum likelihood; (4) retest absolute-agreement ICC; (5) HC3-robust linear regression predicting month-six WHO-5 from FORP/10, baseline WHO-5, PHQ-4, family support, age, sex, stigma concern and diagnosis; (6) R² increase versus a model omitting FORP; (7) exploratory FORP×family support interaction; (8) secondary logistic regression for generated deterioration. Continuous-ML omega and raw-score correlation are **not replacements for an ordinal WLSMV CFA**. The accompanying `scripts/ordinal_cfa.R` specifies the recommended future analysis using `lavaan`. No factor-model fit indices are claimed as computed here.

The future empirical study should include a prespecified sample-size calculation for the continuous outcome, attrition sensitivity analysis (e.g. multiple imputation under MAR plus MNAR scenarios), residual diagnostics, model calibration and clinically meaningful interpretation. Diagnosis groups with low frequency should not be overinterpreted, and subgroup tests must be limited.

## Results

### Flow and baseline characteristics

360 observations were generated at baseline and 303 (84.2%) had a recorded month-six score; 57 records were assigned missing six-month outcomes. Mean age was 42.1 years (SD 12.7), and 222 (61.7%) were coded female. Diagnosis groups were: depression 122, anxiety 121, bipolar disorder 47, OCD 46, and other 24. Baseline FORP total was 18.28 (SD 11.15), with baseline WHO-5 61.92; six-month observed WHO-5 mean was 58.61.

### Illustrative psychometric indices

Alpha was 0.948. A continuous-likelihood one-factor approximation yielded omega=0.948; test–retest ICC(A,1) was 0.954 for 65 selected stable synthetic records. Because item thresholds and common-factor loading strength were built into the generator, none of these estimates establish the actual scale's performance in Turkish psychiatric patients. Ordinal CFA, differential item functioning, measurement invariance and qualitative content validity remain pending actual data.

### Primary prospective demonstration

Among 303 complete records, the adjusted WHO-5 difference for each ten-point higher baseline FORP score was **-2.13 points** (95% CI -3.97 to -0.30; p=0.023). The full-model R² was 0.482 compared with 0.470 for the base model, giving a modest increment (ΔR²=0.011). The family support interaction coefficient was -0.06 (p=0.937), providing no evidence of an interaction in these generated records.

### Secondary illustrative event model

51 of 303 records (16.8%) were assigned a deterioration event. The adjusted model yielded odds ratio 2.35 per 10 FORP points (95% CI 1.59–3.48; p<.001). The event itself was generated partly from FORP; this result therefore reflects the programmed causal structure, not independently observed clinical deterioration.

## Discussion

This demonstration provides a reproducible implementation of an outpatient-friendly prospective research design using existing short psychometric instruments and two culturally relevant contextual questions. Within a deliberately constructed example, FORP showed a negative longitudinal association with well-being after symptom adjustment, while incremental explained variance was small. Critically, the presence or direction of these coefficients in actual patients cannot be inferred from the simulation.

A study of this nature could help distinguish distress-driven recurrence worry from adaptive monitoring and care seeking, provided prospective outcomes are clinically anchored. A second contribution would be cultural interpretation: the same fear score may have different practical implications depending on family support, confidentiality concerns and the consequences of illness in local social networks. The study should seek disconfirming cases during qualitative interviews, e.g. patients whose families are supportive but who still restrict activity, or those who conceal a diagnosis for rational privacy reasons.

The psychological and social constructs need methodological separation. MSPSS family support measures perceived support, not family coercion or collectivism. A single stigma item measures one concern, not a multidimensional internalized-stigma syndrome. Voluntary disclosure and concealment are context-dependent; neither can automatically be classified as maladaptive. Cultural context does not equal a nationality effect and should not be inferred without within-setting variation.

### Limitations

All records are artificial; coefficients were partially encoded into generating equations. The event indicator is not clinician-verified. Dropout was generated as a function of symptoms and fear, making complete-case analysis potentially biased. Some scales are discretized approximations, not administered authorized questionnaires. Factor analysis used continuous approximate ML rather than ordinal CFA and no measured Turkish content validity exists. A single-center cohort cannot establish causal effects or national generalizability. The number of deterioration events may be insufficient for complex diagnostic subgroup models. No cross-cultural invariance comparison was conducted.

### Implications for an actual thesis

A real study needs a registered protocol, written scale permissions, independent translation, cognitive debriefing, ethical review, sample-size calculations and complete patient-reported outcomes with predefined missing-data handling. The current files are a template that can be populated with subsequently observed data. No claims of actual recruitment, patient consent, favorable institutional review or human research results are made.

## References

1. Coutts-Bain D, Sharpe L, Hunt C. Validation of a transdiagnostic measure of fears of recurrence and progression about mental health conditions. Br J Clin Psychol. 2025;64:757–772. doi:10.1111/bjc.12536.
2. Coutts-Bain D, Sharpe L, Techakesari P, Forrester MA, Hunt C. A mixed-methods review and meta-synthesis of fears of recurrence and progression in people with mental health conditions. Clin Psychol Rev. 2023;105:102342. doi:10.1016/j.cpr.2023.102342.
3. Coutts-Bain D, Sharpe L, Hunt C. A transdiagnostic model of fears of recurrence and progression in people with mental health conditions. J Psychopathol Clin Sci. 2026;135:252–264. doi:10.1037/abn0001040.
4. Eker D, Arkar H. Perceived social support: psychometric properties of the MSPSS in normal and pathological groups in a developing country. Soc Psychiatry Psychiatr Epidemiol. 1995;30:121–126. doi:10.1007/BF00802040.
5. Gagnier JJ, et al. COSMIN reporting guideline for studies on measurement properties of patient-reported outcome measures: version 2.0. Qual Life Res. 2025;34:1901–1911. doi:10.1007/s11136-025-03950-x.
6. von Elm E, et al. The Strengthening the Reporting of Observational Studies in Epidemiology (STROBE) statement. PLoS Med. 2007;4:e296. doi:10.1371/journal.pmed.0040296.
7. The International Test Commission. The ITC Guidelines for Translating and Adapting Tests. 2nd ed. 2017. https://www.intestcom.org/files/guideline_test_adaptation_2ed.pdf.
8. WHO-5 Turkish psychometric study (2020). Reliability and validity of the Turkish version of the WHO-5, in adults and older adults for its use in primary care settings. PubMed PMID:32800004.

## Figure and table legends

**Figure 1:** Generated cohort retention, including 28-day retest subset. **Figure 2:** Individual hypothetical six-month WHO-5 scores and adjusted association with baseline FORP-MHQ. **Figure 3:** Adjusted regression coefficients with HC3 confidence intervals. **Figure 4:** Distribution of generated FORP-MHQ scores. **Supplementary Table S1:** reproducible primary regression model in `results/primary_regression.csv`. **Supplementary Table S2:** exploratory approximate factor loadings in `results/factor_loadings_continuous_approx.csv`.