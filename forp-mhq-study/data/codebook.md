# DATA DICTIONARY

**All IDs and variables represent constructed observations. No direct identifiers.**

| Field | Type | Definition | Missing |
|---|---|---|---|
| id | string | Generated pseudonymous identifier SYN-0001... | No |
| age | integer | Age years (18–75) | No |
| sex_female | 0/1 | Generated sex coding (illustration only) | No |
| diagnosis | category | Depression, Anxiety, Bipolar, OCD, Other | No |
| forp_item_01..10 | ordinal 0..4 | Synthetic 10 ordinal item response codes; **no official Turkish items are supplied** | No |
| forp_total | integer 0..40 | Sum of generated FORP items | No |
| phq4_item_1..4 | ordinal 0..3 | Synthetic PHQ-4 scores | No |
| phq4 | integer 0..12 | Sum of four symptom items | No |
| family_item_1..4 | integer 1..7 | Synthetic MSPSS family items | No |
| mspss_family_mean | float 1..7 | Mean of four family support items | No |
| stigma_concern | integer 0..4 | Single exploratory social disclosure concern item | No |
| primary_feared_consequence | category | Symptoms, Family, Work, Stigma, Autonomy, Other | No |
| who5_item_1..5 | integer 0..5 | Synthetic WHO-5 baseline item response codes | No |
| who5_baseline | 0..100 | 4 × sum of baseline item scores | No |
| who5_m3 | 0..100 | Month-three synthetic well-being | Yes: simulated attrition |
| who5_m6 | 0..100 | Month-six synthetic well-being, primary endpoint | Yes: simulated attrition |
| medication_prescribed | 0/1 | Generated medication status | No |
| mars5_total | 5..25 | Adherence score for medicated only; generated | Missing if unmedicated |
| clinical_deterioration_m6 | 0/1 | Generated illustrative event, not verified relapse | Yes: attrition |
| forp_retest_28d | 0..40 | 28-day generated retest subset | Yes: not retested |

**Data generation bias:** Prognostic associations are encoded into outcome equations. Running inference on these data cannot independently support the hypotheses.