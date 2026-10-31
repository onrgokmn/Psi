# Psychiatric relapse fear: thesis, manuscript and reproducible methods (version 2)

**Research simulation and methodological manuscript template.** There were no human participants, site recruitment, ethical approvals, or licensed Turkish FORP-MHQ translation. The generated associations cannot be represented as empirical clinical findings.

## Expanded deliverables
- `thesis/turkish_full.md`, `thesis/turkish_full.docx`, `thesis/turkish_full.pdf`: long-form specialist psychiatry thesis draft.
- `manuscript/english_full.md`, `.docx`, `.pdf`: full international-journal-style English manuscript with abstract, rationale, reproducible methods, baseline and sensitivity tables, results, discussion and references.
- `slides/defense_full.pptx` and `.pdf`: 35-slide white-background, 16:9 editable thesis-defense presentation.
- `data/synthetic_cohort.csv`: generated, item-level records, no identifiable or clinical patient data.
- `scripts/expanded_analysis.py`: analysis consistency checks, attrition weighting and pattern-mixture delta sensitivity.
- `scripts/generate_and_analyze.py`: original seed-based synthetic data generator (original paths expect the original directory structure).
- `scripts/ordinal_cfa.R`: unexecuted ordinal CFA template intended for authorized real translated scale responses.
- `results/`: machine-generated and source-backed model coefficients, baseline descriptives, missingness and sensitivity outcomes.
- `figures/`: baseline, cohort flow, attrition and model results.

## Scientific interpretation
The generator explicitly embeds a negative FORP contribution to six-month WHO-5. The estimated coefficient is therefore *not independent support* for the hypothesis. Current alpha/ICC summarize engineered ordinal item codes; they do not confer Turkish psychometric validity. No interview text or qualitative theme is attributed to patients. Before clinical use, secure permission, ethical approval, translation/cognitive debriefing, preregistered sample-size calculations and real prospectively collected measurements.

## Key demonstrator numbers
- N=360 generated baseline records; 303 with 6-month outcomes; 57 without.
- Adjusted regression per 10 FORP points: β=-2.135 (95% CI -3.974 to -0.296; p=0.0229).
- Model ΔR²=0.01134. IPW estimate β=-2.133 (95% CI -3.973 to -0.292).
- Ten-item alpha=0.948, retest ICC=0.954 in 65 generated pairs; not observed Turkish validation.

## Rebuild steps
1. `python scripts/expanded_analysis.py` rebuilds expanded numeric summaries and figures from `data/synthetic_cohort.csv`.
2. Read `manuscript/english_full.md` and `thesis/turkish_full.md` for the exact narrative, table interpretations and references.
3. Install `python-docx`, `pandoc`, and LibreOffice if DOCX/PDF regeneration is needed.
4. `python scripts/build_deck.py` creates editable 35-slide PPTX (requires python-pptx and matplotlib).

_Authorship, ethics, site permissions and declarations must be completed by actual researchers before human recruitment or external submission._

Full deliverables and numeric analysis are supplied as a versioned archive in the ChatGPT conversation. The repository description alone is not a completed empirical research manuscript.
