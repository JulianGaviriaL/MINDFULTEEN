# Statistical Methods for MINDFULTEEN Mediation Analysis

## Overview

This document describes the statistical methods used to analyze mediation effects in the MINDFULTEEN study, examining the relationship between mindfulness intervention, hormonal biomarkers, and psychological outcomes.

---

## 1. Study Design

### 1.1 Sample
- **N**: 48 adolescents
- **Design**: Within-subjects pre-post intervention
- **Time Points**: V1 (baseline) and V2 (post-intervention)

### 1.2 Variables
- **Independent Variable (X)**: Time point (V1 vs V2)
- **Mediator (M)**: CAMM (Child and Adolescent Mindfulness Measure)
- **Dependent Variables (Y)**: Hormonal biomarkers (Testosterone, Estradiol, Cortisol, DHEA-S)

---

## 2. Mediation Analysis Framework

### 2.1 Causal Mediation Model

The analysis follows the potential outcomes framework for causal mediation (Imai et al., 2010):

```
        CAMM (M)
       /       \
      a         b
     /           \
Time (X) ----c'--- Biomarker (Y)
```

Where:
- **Path a**: Effect of intervention on mediator (CAMM)
- **Path b**: Effect of mediator on outcome, controlling for intervention
- **Path c'**: Direct effect of intervention on outcome (ACDE)
- **Indirect effect (ab)**: ACME = a × b

### 2.2 Effect Definitions

| Effect | Definition | Formula |
|--------|------------|---------|
| **ACME** | Average Causal Mediation Effect | E[Y(1, M(1)) - Y(1, M(0))] |
| **ACDE** | Average Controlled Direct Effect | E[Y(1, m) - Y(0, m)] |
| **Total Effect** | Combined direct + indirect | ACME + ACDE |
| **Proportion Mediated** | Relative contribution of indirect path | ACME / Total Effect |

---

## 3. Model Specification

### 3.1 Mediator Model (Path a)

```
CAMM = β₀ + β₁(Time) + ε₁
```

### 3.2 Outcome Model (Paths b and c')

```
Biomarker = γ₀ + γ₁(Time) + γ₂(CAMM) + ε₂
```

Where:
- β₁ represents path a
- γ₂ represents path b
- γ₁ represents path c' (direct effect)

---

## 4. Diagnostic Tests

### 4.1 Normality Assessment

**Shapiro-Wilk Test**:
- H₀: Residuals are normally distributed
- H₁: Residuals deviate from normality
- α = 0.05

**Decision Rule**: If p < 0.05, normality assumption is violated.

### 4.2 Heteroscedasticity Assessment

**Breusch-Pagan Test**:
- H₀: Homoscedasticity (constant variance)
- H₁: Heteroscedasticity (non-constant variance)
- α = 0.05

**Decision Rule**: If p < 0.05, heteroscedasticity is present.

### 4.3 Multicollinearity Assessment

**Variance Inflation Factor (VIF)**:
- VIF < 5: No concern
- VIF 5-10: Moderate multicollinearity
- VIF > 10: Severe multicollinearity

### 4.4 Autocorrelation Assessment

**Durbin-Watson Test**:
- Statistic range: 0-4
- DW ≈ 2: No autocorrelation
- DW < 1.5: Positive autocorrelation
- DW > 2.5: Negative autocorrelation

### 4.5 Outlier Detection

**Method**: Studentized residuals
- Outlier threshold: |residual| > 2.5 standard deviations

---

## 5. Robust Standard Errors

### 5.1 Heteroscedasticity-Consistent (HC) Estimators

Given detected heteroscedasticity and small sample size, we employed HC3 robust standard errors:

**HC0 (White, 1980)**:
```
V̂_HC0 = (X'X)⁻¹ (Σ û²ᵢ xᵢxᵢ') (X'X)⁻¹
```

**HC3 (Davidson & MacKinnon, 1993)**:
```
V̂_HC3 = (X'X)⁻¹ (Σ [ûᵢ/(1-hᵢᵢ)]² xᵢxᵢ') (X'X)⁻¹
```

Where:
- ûᵢ = residual for observation i
- hᵢᵢ = leverage (diagonal of hat matrix)
- xᵢ = predictor vector for observation i

### 5.2 HC3 Selection Rationale

HC3 was selected based on:
1. Superior small-sample performance (Long & Ervin, 2000)
2. Conservative confidence interval coverage
3. Robustness to heteroscedasticity
4. Recommended when n < 250

---

## 6. Bootstrap Confidence Intervals

### 6.1 Procedure

1. Resample n observations with replacement
2. Fit mediation models to bootstrap sample
3. Calculate ACME, ACDE, Total Effect
4. Repeat B = 5,000 times
5. Construct percentile confidence intervals

### 6.2 Confidence Interval Construction

**Percentile Method**:
```
CI_95% = [θ̂*(α/2), θ̂*(1-α/2)]
```

Where θ̂* represents the bootstrap distribution of the effect estimate.

---

## 7. Multiple Testing Correction

### 7.1 Benjamini-Hochberg (BH) Procedure

To control the False Discovery Rate (FDR) at α = 0.05:

1. Order p-values: p₍₁₎ ≤ p₍₂₎ ≤ ... ≤ p₍ₘ₎
2. Find largest k where p₍ₖ₎ ≤ (k/m) × α
3. Reject H₀ for all hypotheses with p ≤ p₍ₖ₎

### 7.2 Application

Applied to all ACME, ACDE, and Total Effect p-values across biomarkers (m = 15 tests).

---

## 8. Effect Size Calculations

### 8.1 Cohen's d (Paired Samples)

```
d = (M_V2 - M_V1) / SD_change
```

**Interpretation**:
- Small: d = 0.20
- Medium: d = 0.50
- Large: d = 0.80

### 8.2 Proportion Mediated

```
PM = ACME / Total_Effect
```

**Note**: PM is only interpretable when ACME and Total Effect have the same sign.

---

## 9. Software and Implementation

### 9.1 Statistical Software
- **R** (version 4.x)
- Key packages:
  - `mediation`: Causal mediation analysis
  - `sandwich`: Robust standard errors
  - `lmtest`: Diagnostic tests
  - `car`: VIF calculation
  - `boot`: Bootstrap methods

### 9.2 Reproducibility

- Random seed set for bootstrap resampling
- Bootstrap iterations: B = 5,000
- Confidence level: 95%

---

## 10. Sensitivity Analyses

### 10.1 Sequential Ignorability

The key identifying assumption for causal mediation is sequential ignorability:

1. Treatment assignment is ignorable given pre-treatment covariates
2. Mediator is ignorable given treatment and pre-treatment covariates

**Sensitivity Analysis**: We examined how violations of assumption 2 would affect ACME estimates using the sensitivity parameter ρ (correlation between mediator and outcome error terms).

### 10.2 Outlier Sensitivity

Analyses were repeated excluding identified outliers to assess robustness of findings.

### 10.3 Log-Transformation

Biomarker concentrations were analyzed both in original units and log-transformed to address non-normality.

---

## 11. Limitations

### 11.1 Methodological Limitations

1. **Within-subjects design**: Cannot fully establish temporal precedence
2. **Single mediator**: CAMM may not capture all mindfulness dimensions
3. **Sample size**: Limited power for detecting small indirect effects
4. **Assumption violations**: Some models showed heteroscedasticity and non-normality

### 11.2 Mitigation Strategies

| Limitation | Mitigation |
|------------|------------|
| Heteroscedasticity | HC3 robust standard errors |
| Non-normality | Bootstrap confidence intervals |
| Small sample | Conservative HC3 estimator |
| Multiple testing | BH correction |

---

## References

- Davidson, R., & MacKinnon, J. G. (1993). *Estimation and inference in econometrics*. Oxford University Press.
- Hayes, A. F. (2018). *Introduction to mediation, moderation, and conditional process analysis* (2nd ed.). Guilford Press.
- Imai, K., Keele, L., & Tingley, D. (2010). A general approach to causal mediation analysis. *Psychological Methods*, 15(4), 309-334.
- Long, J. S., & Ervin, L. H. (2000). Using heteroscedasticity consistent standard errors in the linear regression model. *The American Statistician*, 54(3), 217-224.
- MacKinnon, D. P. (2008). *Introduction to statistical mediation analysis*. Routledge.
- Preacher, K. J., & Hayes, A. F. (2008). Asymptotic and resampling strategies for assessing and comparing indirect effects in multiple mediator models. *Behavior Research Methods*, 40(3), 879-891.
- White, H. (1980). A heteroskedasticity-consistent covariance matrix estimator and a direct test for heteroskedasticity. *Econometrica*, 48(4), 817-838.

---

*Document prepared for MINDFULTEEN manuscript submission*
*Last updated: December 2024*
