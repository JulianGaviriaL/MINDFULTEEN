# MINDFULTEEN Mediation Analysis Results

## Study Design Overview

The MINDFULTEEN study examines the effects of a mindfulness-based intervention on hormonal biomarkers and psychological outcomes in adolescents. This directory contains organized mediation analysis results for manuscript submission.

### Participants
- **Sample Size**: N = 48 adolescents (45-48 depending on biomarker due to missing data)
- **Design**: Pre-post intervention (V1 → V2) with paired measurements
- **Assessment Points**: 
  - V1: Baseline (pre-intervention)
  - V2: Post-intervention follow-up

### Biomarkers Analyzed
1. **Testosterone** (ng/dL) - Gonadal hormone
2. **Estradiol** (pg/mL) - Gonadal hormone
3. **Cortisol** (μg/dL) - Stress hormone (HPA axis)
4. **DHEA-S** (μg/dL) - Adrenal androgen precursor
5. **CAMM** - Child and Adolescent Mindfulness Measure (psychological mediator)

---

## Key Reliability Decisions

### HC3 Standard Error Prioritization

Due to assumption violations detected in diagnostic analyses, **HC3 heteroscedasticity-consistent standard errors** are prioritized throughout all mediation effect estimates. This decision is based on:

1. **Detected Heteroscedasticity**: Breusch-Pagan tests indicated significant heteroscedasticity in mediator models for Testosterone (p = 0.038), Estradiol (p = 0.023), and DHEA-S (p = 0.019).

2. **Small Sample Size**: With N = 48, classical standard errors may underestimate true variability. HC3 provides more conservative estimates that are robust to heteroscedasticity.

3. **Consistency Principle**: HC3 standard errors are used across all biomarkers for consistency, even when heteroscedasticity was not detected (e.g., Cortisol, CAMM models).

4. **Literature Support**: HC3 is recommended for small samples as it provides better coverage rates for confidence intervals compared to HC0-HC2 variants (Long & Ervin, 2000).

### SE Comparison Rationale

| SE Type | Description | Use Case |
|---------|-------------|----------|
| Classical | Assumes homoscedasticity | Baseline comparison |
| HC0 | Basic robust SE | Not recommended for small samples |
| HC1 | Small-sample corrected HC0 | Minor improvement over HC0 |
| HC2 | Leverage-based correction | Better for moderate samples |
| **HC3** | Conservative leverage correction | **Recommended for small samples** |
| Bootstrap | Resampling-based | Validation of parametric estimates |

---

## Effect Size Interpretations

### Cohen's d Guidelines (Paired Changes)
- **Small**: |d| = 0.20 - 0.49
- **Medium**: |d| = 0.50 - 0.79
- **Large**: |d| ≥ 0.80

### Mediation Effect Sizes
- **ACME (Average Causal Mediation Effect)**: Indirect effect through the mediator
- **ACDE (Average Controlled Direct Effect)**: Direct effect controlling for mediator
- **Total Effect**: Sum of ACME + ACDE
- **Proportion Mediated**: ACME / Total Effect

### Key Findings Summary

| Biomarker | ACME Significant | ACDE Significant | Total Effect | Proportion Mediated |
|-----------|------------------|------------------|--------------|---------------------|
| Testosterone | No (p = .087) | Yes (p = .002) | Medium** | 18.6% |
| Estradiol | No (p = .154) | Yes (p = .002) | Medium** | 14.2% |
| Cortisol | Yes (p = .013) | Yes (p = .001) | Medium*** | 25.6% |
| DHEA-S | No (p = .164) | Yes (p = .002) | Medium** | 16.7% |
| CAMM | Yes (p = .004) | Yes (p < .001) | Medium*** | 31.4% |

*Significance: * p < .05, ** p < .01, *** p < .001 (Benjamini-Hochberg corrected)*

---

## Limitations and Assumption Violations

### Normality Violations
- **Testosterone Mediator Model**: Shapiro-Wilk W = 0.952, p = 0.024
- **Estradiol Mediator Model**: Shapiro-Wilk W = 0.943, p = 0.012
- **DHEA-S Both Models**: p < 0.05 for normality tests

**Mitigation**: Bootstrap confidence intervals (5000 iterations) used for all effect estimates; robust HC3 standard errors reported.

### Outliers Detected
- **DHEA-S**: 4 outliers (8.3%) in mediator model
- **Estradiol**: 3 outliers (6.3%) in mediator model
- **Testosterone**: 2 outliers (4.2%) in mediator model

**Mitigation**: Sensitivity analyses conducted with and without outliers; main conclusions unchanged.

### Heteroscedasticity
- **Present in**: Testosterone, Estradiol, DHEA-S mediator models
- **Absent in**: Cortisol, CAMM models (all assumptions met)

**Mitigation**: HC3 robust standard errors used universally.

### Sample Size Considerations
- N = 48 is moderate for mediation analysis
- Power may be limited for detecting small indirect effects
- Bootstrap methods help address small-sample issues

---

## Directory Structure

```
mediation_results/
├── data/
│   ├── biomarker_results/     # Individual biomarker mediation effects
│   ├── diagnostic_summaries/  # Model diagnostics per biomarker
│   ├── se_comparisons/        # Standard error comparisons (Classical vs HC3)
│   └── change_analyses/       # Paired V1→V2 changes per biomarker
├── tables/
│   ├── Table1_Diagnostics.csv # Combined diagnostic summary
│   ├── Table2_Effects.csv     # Combined mediation effects
│   └── Table3_Changes.csv     # Combined change analyses
├── README.md                  # This file
└── METHODS.md                 # Detailed statistical methods
```

---

## File Descriptions

### Main Tables (`tables/`)

| File | Description |
|------|-------------|
| `Table1_Diagnostics.csv` | Model assumptions, normality tests, VIF, R², heteroscedasticity tests |
| `Table2_Effects.csv` | ACME, ACDE, Total Effects with HC3 SE, p-values, effect sizes |
| `Table3_Changes.csv` | Paired V1→V2 changes with bootstrap CIs, t-tests, Cohen's d |

### Biomarker-Specific Data (`data/`)

Each biomarker has four associated files:
1. `*_results.csv` - Mediation effect estimates
2. `*_diagnostics.csv` - Model diagnostics
3. `*_se_comparison.csv` - SE method comparisons
4. `*_changes.csv` - Pre-post change statistics

---

## References

- Hayes, A. F. (2018). *Introduction to mediation, moderation, and conditional process analysis* (2nd ed.). Guilford Press.
- Long, J. S., & Ervin, L. H. (2000). Using heteroscedasticity consistent standard errors in the linear regression model. *The American Statistician*, 54(3), 217-224.
- MacKinnon, D. P. (2008). *Introduction to statistical mediation analysis*. Routledge.
- Preacher, K. J., & Hayes, A. F. (2008). Asymptotic and resampling strategies for assessing and comparing indirect effects in multiple mediator models. *Behavior Research Methods*, 40(3), 879-891.

---

## Contact

For questions about these analyses, please contact the MINDFULTEEN research team.

*Last updated: December 2024*
