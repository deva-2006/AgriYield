# AgriYield: Detailed Research Methodology

This document outlines the mathematical formulations, preprocessing pipelines, validation protocols, and architectural specifications underpinning **AgriYield**.

---

## 1. End-to-End Workflow Architecture

```
[ RAW CENSUS DATASET (19,689 records) ]
                  │
                  ▼
[ DATA AUDIT & UNDERSTANDING ]
  - Verify completeness (100.0%, 0 nulls, 0 duplicates)
  - Examine distributions, skewness, and extreme values
                  │
                  ▼
[ REPRODUCIBLE DATA CLEANING ]
  - Trim trailing whitespace in categorical strings
  - Physical non-negativity constraint verification
  - Isolate Coconut scale disparity (Nuts/ha vs Tonnes/ha)
  - Crop-stratified Tukey's IQR boundaries
                  │
                  ▼
[ EXPLORATORY & STATISTICAL HYPOTHESIS TESTING ]
  - 14 interactive Plotly diagnostic charts
  - One-Way ANOVA & Kruskal-Wallis non-parametric variance tests
  - Pearson & Spearman correlations with p-value significance
  - Simpson's Paradox validation across crop strata
                  │
                  ▼
[ LEAKAGE-FREE FEATURE ENGINEERING ]
  - Excise post-harvest Production: Avoid Yield = Production / Area identity
  - Derive agronomic intensity ratios: Fertilizer/Area, Pesticide/Area
  - Compute technological diffusion index: Year - min(Year)
  - Logarithmic transformations: ln(1 + Area), ln(1 + Rainfall)
                  │
                  ▼
[ TIME-AWARE TRAIN / TEST PARTITION ]
  - Training Period: 1997–2015 (15,404 samples)
  - Holdout Evaluation Period: 2016–2020 (4,285 samples)
  - 5-Fold Cross-Validation on training subset
                  │
                  ▼
[ REGRESSION MODEL BENCHMARKING ]
  - Linear Regression (Ridge L2 regularization)
  - Decision Tree Regressor
  - Random Forest Regressor
  - Gradient Boosting Regressor
  - Log-transformed target regressor: TransformedTargetRegressor(func=log1p)
                  │
                  ▼
[ EVALUATION & MODEL INTERPRETATION ]
  - Calculate out-of-sample MAE, MSE, RMSE, R²
  - Generate Actual vs Predicted & Residual diagnostic plots
  - Extract global Gini importances and parent feature contributions
                  │
                  ▼
[ PRESENTATION LAYER: STREAMLIT DASHBOARD ]
  - Interactive multi-page decision support system
```

---

## 2. Mathematical Formulations

### 2.1 Target Productivity Definition
$$\text{Yield}_i = \frac{\text{Production}_i}{\text{Area}_i}$$
*Units*: Metric Tonnes per Hectare ($\text{t/ha}$) for arable field crops; Nuts per Hectare for Coconut.

### 2.2 Leakage Prevention Constraint
Let the full feature space recorded in the census be:
$$\mathcal{S} = \{\text{Crop}, \text{State}, \text{Season}, \text{Crop\_Year}, \text{Area}, \text{Production}, \text{Rainfall}, \text{Fertilizer}, \text{Pesticide}\}$$
The predictive feature subspace $\mathcal{X}$ is strictly defined as:
$$\mathcal{X} = \mathcal{S} \setminus \{\text{Production}, \text{Yield}\}$$

### 2.3 Agronomic Input Intensity Ratios
$$\text{Fertilizer\_Intensity}_i = \frac{\text{Fertilizer}_i}{\text{Area}_i} \quad [\text{kg/ha}]$$
$$\text{Pesticide\_Intensity}_i = \frac{\text{Pesticide}_i}{\text{Area}_i} \quad [\text{kg/ha}]$$

### 2.4 Target Logarithmic Transformation
To account for biological right-skewness and ensure non-negative predictions:
$$z_i = \ln(1 + y_i)$$
The estimated physical yield $\hat{y}_i$ is obtained via the inverse mapping:
$$\hat{y}_i = \exp(\hat{z}_i) - 1$$

---

## 3. Evaluation Metrics

Model performance is evaluated on the holdout test set ($N_{\text{test}} = 4,285$) using:

1. **Mean Absolute Error (MAE)**:
   $$\text{MAE} = \frac{1}{N} \sum_{i=1}^N |y_i - \hat{y}_i|$$
2. **Mean Squared Error (MSE)**:
   $$\text{MSE} = \frac{1}{N} \sum_{i=1}^N (y_i - \hat{y}_i)^2$$
3. **Root Mean Squared Error (RMSE)**:
   $$\text{RMSE} = \sqrt{\frac{1}{N} \sum_{i=1}^N (y_i - \hat{y}_i)^2}$$
4. **Coefficient of Determination ($R^2$)**:
   $$R^2 = 1 - \frac{\sum_{i=1}^N (y_i - \hat{y}_i)^2}{\sum_{i=1}^N (y_i - \bar{y})^2}$$

All metrics are computed on the original physical scale ($\text{Tonnes/Ha}$).
