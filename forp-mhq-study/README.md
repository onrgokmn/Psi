# Relapse fear and six-month well-being: psychiatry thesis reproducibility package

> ⚠️ **Synthetic methodological demonstrator. No patients were recruited; no ethics approval, permission to translate an instrument, or actual statistical validation is claimed.** The complete article-shaped text is not submission-ready empirical evidence.

## Clinical question
Does fear of psychiatric recurrence contribute to subsequent well-being beyond current symptoms, and how might family support and social disclosure concerns contextualize this association?

## Contents
- `manuscript/turkish_thesis_draft.md`: complete Turkish thesis draft (structured intro, aims, methods, demonstration results, discussion, bibliography)
- `manuscript/english_manuscript.md`: journal-style English article with abstract, methods and calculated results
- `manuscript/structured_abstract.md`: abstract
- `protocol/preregistration_protocol.md`: registered-study-ready plan (unapproved)
- `data/synthetic_cohort.csv`: complete generated patient-like data (local bundle)
- `data/codebook.md`: variables and constraints
- `scripts/generate_and_analyze.py`: fixed-seed generation and analytical calculations (Python)
- `scripts/ordinal_cfa.R`: ordinal CFA and omega after genuine Turkish scale permission and patient recruitment
- `results/summary.json`, `results/primary_regression.csv`: computed outputs
- `slides/defense_deck.pptx`: widescreen defense presentation (local bundle)
- `slides/defense_slides.html`: portable GitHub-viewable slide source
- `figures/*.png`: figures used in manuscript and slides (local bundle)

## Reproduce
`python scripts/generate_and_analyze.py` (Python 3.10+; numpy, scipy, pandas, sklearn, statsmodels, matplotlib). Data are seeded at 20261031; outputs reproduce the demonstration from scratch. For ordinal WLSMV model on subsequently observed data, use `scripts/ordinal_cfa.R` with R packages lavaan and semTools.

## Interpretation
The simulator builds a negative effect of FORP into the WHO-5 data-generating mechanism. Apparent statistical significance is expected and not evidence of an observed clinical association. The results must be replaced after real ethical patient recruitment and data collection. Avoid uploading real clinical datasets to public GitHub. Copyrighted scale item wording is not distributed.

## Source verification
- Coutts-Bain et al., BJCP 2025, https://doi.org/10.1111/bjc.12536
- Coutts-Bain et al., Clinical Psychology Review 2023, https://doi.org/10.1016/j.cpr.2023.102342
- Coutts-Bain et al., Journal of Psychopathology and Clinical Science 2026, https://doi.org/10.1037/abn0001040
- Gagnier et al., COSMIN v2 2025, https://doi.org/10.1007/s11136-025-03950-x
- Eker & Arkar, MSPSS Turkish, https://doi.org/10.1007/BF00802040