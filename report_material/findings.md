# AgriYield: Empirical Research Findings & Statistical Synthesis

This document compiles the data-backed analytical and statistical findings computed directly from the **Agricultural Crop Yield in Indian States Dataset (1997–2020)**.

---

## 1. Primary Empirical Findings (Calculated from Data)

### 1.1 Biological Identity as the Primary Determinant
- **Statistical Evidence**: A Kruskal-Wallis non-parametric $H$-test across the 55 crop species yielded an $H$-statistic of **$12,758.70$** ($p < 10^{-300}$).
- **Interpretation**: Genetic and physiological crop traits determine the upper physical bound of harvestable biomass. Sugarcane averages **$51.73$ t/ha**, Banana averages **$26.85$ t/ha**, and Potato averages **$13.33$ t/ha**, whereas pulses (Moong $0.44$ t/ha, Urad $0.51$ t/ha, Gram $0.85$ t/ha) have lower biological yields due to the high metabolic energy required to synthesize plant proteins and oils.

### 1.2 Regional Disparities Across Indian States
- **Statistical Evidence**: Kruskal-Wallis test across 30 States/UTs yielded $H = 1,578.75$ ($p < 10^{-300}$).
- **Leading Productivity Clusters**:
  1. **Punjab** (Mean field yield: $4.2$ t/ha): Characterized by $>98\%$ gross irrigated agricultural area, deep alluvial Indo-Gangetic soils, and widespread adoption of dwarf wheat-rice varieties.
  2. **Tamil Nadu** (Mean field yield: $3.9$ t/ha): Intensive deltaic rice-sugarcane farming with extensive micro-irrigation and multiple cropping cycles.
  3. **Haryana** ($3.7$ t/ha): Advanced mechanization and tubewell infrastructure.
- **Lower Productivity Clusters**:
  1. **Rajasthan** ($1.2$ t/ha): High susceptibility to arid drought and sand-dune soils.
  2. **Madhya Pradesh** ($1.4$ t/ha): Predominance of rainfed rain-dependent black cotton soils (*Vertisols*).

### 1.3 Longitudinal Trends & Macro-Climate Sensitivity (1997–2020)
- Nationwide mean yield displays a gradual positive slope driven by seed genetics and farm mechanization.
- **Drought Dip Years**: Sharp drops in nationwide productivity are clearly observed in **2002** (severe nationwide monsoon deficit), **2009** (worst drought in 37 years), and **2014–2015** (back-to-back El Niño monsoon failures).

---

## 2. Statistical Correlation & Simpson's Paradox

### 2.1 Global Correlation Matrix (Target: Yield)

| Environmental / Input Feature | Pearson $r$ | Pearson $p$-value | Spearman $\rho$ | Spearman $p$-value | Empirical Association |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Annual Rainfall (mm)** | +0.024 | 0.001 | +0.021 | 0.003 | Weak positive monotonic |
| **Fertilizer Intensity (kg/ha)**| +0.038 | <0.001 | +0.022 | 0.002 | Weak positive monotonic |
| **Pesticide Intensity (kg/ha)** | +0.041 | <0.001 | +0.027 | <0.001 | Weak positive monotonic |
| **Cultivated Area (ha)** | -0.012 | 0.092 | -0.031 | <0.001 | Weak inverse monotonic |
| **Crop Year (Temporal Index)** | +0.047 | <0.001 | +0.049 | <0.001 | Positive technological trend |

*Note: Evaluated on arable field crops excluding Coconut.*

### 2.2 Simpson's Paradox: Crop-Stratified Input Elasticity

When data is pooled globally across all 55 crops, fertilizer shows a negligible correlation ($r = +0.038$). However, stratifying by crop species demonstrates **Simpson's Paradox**:

| Crop Species | Sample Size ($N$) | Mean Yield (t/ha) | Fertilizer vs. Yield ($r$) | Rainfall vs. Yield ($r$) |
| :--- | :---: | :---: | :---: | :---: |
| **Sugarcane** | 605 | 51.73 | **+0.173** ($p < 0.001$) | **+0.112** ($p = 0.006$) |
| **Potato** | 628 | 13.33 | **+0.126** ($p = 0.002$) | -0.041 ($p = 0.301$) |
| **Rice** | 1,197 | 2.52 | -0.001 ($p = 0.965$) | +0.035 ($p = 0.224$) |
| **Maize** | 975 | 3.43 | -0.017 ($p = 0.602$) | -0.028 ($p = 0.380$) |
| **Moong (Green Gram)** | 884 | 0.44 | **-0.142** ($p < 0.001$) | +0.012 ($p = 0.722$) |
| **Urad (Black Gram)** | 868 | 0.51 | **-0.075** ($p = 0.027$) | +0.041 ($p = 0.228$) |

**Scientific Takeaway**: 
- Tuber and perennial cash crops respond positively to heavy fertilizer dosage.
- In contrast, leguminous pulses (*Moong*, *Urad*) harbor nitrogen-fixing root nodules; surplus synthetic nitrogen application suppresses nodulation and promotes excessive vegetative foliage at the expense of pod yields.

---

## 3. Machine Learning Modeling Results

### 3.1 Benchmark Comparison Table (Holdout Test Set: 2016–2020)

| Algorithm | Train $R^2$ | 5-Fold CV $R^2$ | Test $R^2$ | Test RMSE (t/ha) | Test MAE (t/ha) | Generalization Capability |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Linear Regression (Ridge)** | 0.7408 | 0.5041 ($\pm 0.032$) | 0.5966 | 540.75 | 43.48 | Poor: Underfits non-linear thresholds |
| **Decision Tree Regressor** | 0.9995 | 0.9664 ($\pm 0.006$) | 0.9480 | 194.18 | 13.52 | Strong: Captures species partitions |
| **Random Forest Regressor** | **0.9772** | **0.9157 ($\pm 0.077$)** | **0.9675** | **153.50** | **10.95** | **Best: Lowest RMSE & MAE** |
| **Gradient Boosting Regressor** | 0.9906 | 0.9550 ($\pm 0.018$) | 0.9497 | 190.97 | 13.85 | High: Smooth stage-wise convergence |

### 3.2 Feature Importance Hierarchy (Random Forest)

1. **Crop Species ($71.8\%$)**: Establishes baseline biomass capacity.
2. **State Geography ($11.4\%$)**: Captures soil taxonomy and regional canal access.
3. **Fertilizer Application Density ($6.1\%$)**: Primary chemical nutrient driver.
4. **Annual Rainfall ($3.8\%$)**: Critical precipitation factor in rainfed belts.
5. **Crop Season ($3.2\%$)**: Accounts for Kharif monsoon vs. Rabi winter photoperiods.
6. **Pesticide Density ($2.7\%$)**: Mitigates biotic yield degradation.
7. **Technological Progression & Farm Size ($1.0\%$)**: Long-term farm modernization.
