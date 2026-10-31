# FORP-MHQ · Peer-Reviewed Revision v3
**Status:** Protocol and audited research simulation; no human research, clinical findings, ethics approval, or authorized Turkish scale validation are claimed.

## Purpose
A single-primary-hypothesis prospective psychiatry cohort design examines the conditional relationship of baseline recurrence fear (FORP-MHQ) with six-month WHO-5 subjective well-being, while treating patient-reported family support and disclosure concern as separate context variables. Nüks/relapse and subjective well-being are not interchangeable outcomes.

## Review outcome
**Major revision.** A detailed 26-point reviewer report, fully revised English manuscript, Turkish expanded specialist-thesis draft, 42-slide presentation, prespecified real-world statistical analysis plan, corrected analysis scripts, figures and generated CSV are included in the complete versioned download supplied in the originating ChatGPT conversation.

## Specific corrections
1. A negative FORP slope was explicitly programmed in the synthetic outcome model, so p=0.023 cannot establish a clinical hypothesis.
2. Generated response patterns are **not monotone**: 273 both visits, 47 month-three only, 30 month-six only, 10 neither. Earlier sequential attrition diagram is unsuitable.
3. Single-imputation confidence intervals in an earlier missingness sensitivity table understated uncertainty; these were removed. New point-only stress tests vary both unseen average WHO-5 and unseen FORP slope.
4. Generated 28-day retest pairs were selected based on future month-six outcomes and observation status. This design cannot estimate real-world test–retest reliability. The future subgroup must be recruited at baseline.
5. Adjusted simulated beta is -2.1347 WHO-5 points per 10 FORP points (HC3 CI -3.9739 to -0.2955), versus crude -7.502; ΔR² is only 0.01134. Clinical relevance and prediction performance are not established.
6. A one-item disclosure worry measure is not a validated mental-illness stigma scale. Perceived family support is not equivalent to a national culture.
7. Noncentral-F power sensitivity (12 coefficients, α=.05, 80% power): partial R²=.01 needs ~779 six-month completers, .02 ~387, .03 ~256. With 16% attrition, approximately 928, 461, 305 initial participants respectively. CFA requirements need separate consideration.
8. Explicitly require FORP-MHQ rights-holder consent, cognitive debriefing, Turkish ordinal CFA, stable-subgroup ICC, real patient informed consent, ethics authorization, privacy plan and prospective clinical recruitment.

## Accessible source from v2
See [expanded English source](../forp-mhq-study-v2/manuscript/english_full.md), [Turkish thesis source](../forp-mhq-study-v2/thesis/turkish_full.md), [original reproducible numerical code](../forp-mhq-study-v2/scripts/expanded_analysis.py), and [generated CSV](../forp-mhq-study-v2/data/synthetic_cohort.csv). These are **prior versions**; do not use them as revised v3 without applying the documented corrections.

## Publication boundary
The revised paper is an academic manuscript/protocol **template**, not a publishable clinical original research paper without actual ethically collected patient data. Never commit patient-identifying or health data to a public GitHub repository.
