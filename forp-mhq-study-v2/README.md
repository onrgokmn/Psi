# Fear of psychiatric recurrence: full thesis and journal article research package (v2)

**Status: computational demonstration and prerecruitment study protocol.** This is **not** a human-participant study. All records, associations, internal-consistency values, test-retest values, and follow-up outcomes in the Results are synthetic and **must not be presented as clinical evidence or as a completed Turkish validation.** No ethics approval, patient recruitment, patient interviews, or authorized Turkish adaptation of FORP-MHQ has occurred.

## Scientific question

Does baseline fear of psychiatric relapse explain six-month mental well-being beyond concurrent symptoms, and do individual perceptions of family support and mental-illness disclosure alter that relationship? The design combines transdiagnostic prospective measurement with psychometric translation and an embedded qualitative interview protocol for future real-world research.

## Source files stored here

- [English full manuscript](manuscript/english_full.md): introduction, literature, hypotheses, methods, baseline and regression results, MNAR sensitivity scenarios, discussion, declarations and 15 references.
- [Turkish comprehensive thesis draft](thesis/turkish_full.md): clinical rationale, culture-sensitive sampling, statistical analysis, critical interpretation, appendices and references.
- [Synthetic cohort](data/synthetic_cohort.csv): 360 generated anonymized-by-construction rows, baseline and two follow-ups; no patient records.
- [Seeded data generator](scripts/generate_and_analyze.py): recreates synthetic participant-like records and initial analysis.
- [Extended analysis](scripts/expanded_analysis.py): HC3 OLS, incremental R², VIF, attrition modeling, inverse-probability weights, pattern-mixture sensitivity analyses and CSV summaries.
- [R ordinal CFA template](scripts/ordinal_cfa.R): **not executed**; requires a future, authorized and cognitively tested Turkish scale and real participant data.
- [PowerPoint generation script](scripts/build_deck.py): recreates a 35-slide presentation with local dependencies.
- [Numeric model audit](results/expanded_summary.json).
- [Human-research and publication checklist](PROJECT_CHECKLIST.md).

## Delivered separately in the complete archive

Publication-formatted PDF and DOCX versions of the manuscript and thesis, editable PowerPoint and slides PDF, charts, results CSVs, original references and document-generation helpers are included in the downloadable complete archive attached to the ChatGPT conversation. **They are not currently committed to this source-code branch.**

## Reproduce

Python 3.10+ dependencies: numpy, scipy, pandas, statsmodels, matplotlib, scikit-learn, python-pptx. Run from the repository folder:

```bash
python scripts/generate_and_analyze.py
python scripts/expanded_analysis.py
python scripts/build_deck.py
```

The generator has a fixed RNG seed (`20261031`); generated outputs are model-defined, not naturalistic observations. The main model specifically embeds a negative relationship between fear and future WHO-5, so rediscovering the parameter is **not hypothesis confirmation**. The questionnaire's original 10 item texts are not included to avoid implying permission to reproduce or translate it.

## Replacing the simulation with real research

Before any empirical thesis or manuscript submission: verify Turkish adaptation novelty; obtain the original instrument owner's authorization; seek ethics/clinical site permissions; translate and cognitively test wording; justify sample size and interactions; prospectively collect minimal-burden baseline and follow-ups; perform ordinal WLSMV CFA and ICC against a clinically stable repeat test sample; preregister the primary estimand; monitor attrition; conduct and transparently code consented qualitative interviews; and provide accurate author, funding and AI disclosures.

This repository is a serious **study-design and document-production prototype**, not publishable original patient research as it stands.
