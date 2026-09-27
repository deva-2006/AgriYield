# 🌾 AgriYield: Data Science-Based Crop Yield Analysis and Prediction

An academic data science project investigating the environmental, agricultural, spatial, and temporal determinants of crop productivity across India. Built on genuine census records (1997–2020), this repository features a reproducible data science pipeline coupled with a high-performance Streamlit dashboard.

---

## 📌 Project Overview & Objectives

Agricultural crop yield is subject to complex multi-factorial interactions involving crop biology, seasonal weather, fertilizer/pesticide management, and spatial geography. **AgriYield** was engineered to rigorously answer:
1. **Biological Ceilings**: How does crop yield vary across species, administrative regions, and harvest years?
2. **Climate & Agronomic Inputs**: How are rainfall patterns and chemical intensities associated with crop yield?
3. **Forecasting Feasibility**: Can future crop yield be accurately predicted prior to harvest using machine learning while strictly preventing target leakage?
4. **Predictive Drivers**: Which agronomic and environmental features contribute most significantly to predictive performance?

---

## 🏛️ Project Architecture

```
agriyield/
│
├── data/
│   ├── dataset.csv                          # Ingested dataset (19,689 records)
│   └── cleaned_dataset.csv                  # Standardized and audited dataset
│
├── notebooks/
│   └── exploratory_analysis.ipynb           # Fully reproducible Jupyter notebook
│
├── src/
│   ├── __init__.py                          # Package initializer
│   ├── data_loader.py                       # Ingestion, schema verification & audit
│   ├── preprocessing.py                    # String normalization, bounds checking, unit tags
│   ├── eda.py                              # 14 interactive Plotly charts with styling
│   ├── statistical_analysis.py             # Correlations, ANOVA, Kruskal-Wallis, Simpson's Paradox
│   ├── feature_engineering.py              # Agronomic intensities, log transforms, temporal split
│   ├── train_models.py                     # Cross-validation & regression model training
│   ├── evaluate_models.py                  # Model diagnostics, residual analysis & comparison
│   └── prediction.py                       # Live inference engine with confidence intervals
│
├── models/
│   ├── best_model.pkl                      # Serialized Random Forest pipeline
│   ├── model_comparison.json               # Computed train, CV, and holdout test metrics
│   ├── feature_importance.json             # Gini and parent-level feature importances
│   └── test_predictions.csv                # Holdout evaluation predictions
│
├── report_material/
│   ├── project_summary.md                   # Full academic paper (Abstract to References)
│   ├── methodology.md                       # Comprehensive methodology breakdown
│   ├── findings.md                          # Empirical findings calculated from data
│   └── figure_guide.md                      # Internship report figure reference (Figs 1–13)
│
├── app.py                                   # 8-page Streamlit dashboard
├── requirements.txt                         # Python dependencies
└── README.md                                # Project documentation
```

---

## 📊 Dataset Provenance & Properties

- **Source**: Directorate of Economics and Statistics (DES), Ministry of Agriculture and Farmers Welfare, and India Meteorological Department (IMD).
- **Records**: 19,689 complete observations.
- **Attributes**: 10 columns (`Crop`, `Crop_Year`, `Season`, `State`, `Area`, `Production`, `Annual_Rainfall`, `Fertilizer`, `Pesticide`, `Yield`).
- **Temporal Horizon**: 1997 to 2020 (24 continuous years).
- **Spatial Coverage**: 30 Indian States and Union Territories.
- **Taxonomic Diversity**: 55 agricultural crops.
- **Data Completeness**: 100.0% (0 missing values, 0 duplicate rows).

---

## 🛡️ Critical Data Science Integrity: Leakage Prevention

In agricultural accounting, **$\text{Yield} = \text{Production} / \text{Area}$**. 
If post-harvest `Production` were included as an input feature, the algorithm would trivially compute this mathematical identity ($R^2 \approx 1.0$), resulting in fatal data leakage.

In **AgriYield**, `Production` is **strictly excluded** from all predictive modeling. Features are restricted exclusively to pre-harvest agronomic, spatial, climatic, and temporal variables:
- `Crop` (One-hot encoded)
- `State` (One-hot encoded)
- `Season` (One-hot encoded)
- `Crop_Year` & `Year_Index` (Longitudinal technological proxy)
- `Area` & `Log_Area` (Landholding scale)
- `Annual_Rainfall` & `Log_Rainfall` (Hydrological condition)
- `Fertilizer_per_Area` & `Log_Fertilizer_per_Area` (Nutrient application density)
- `Pesticide_per_Area` & `Log_Pesticide_per_Area` (Crop protection intensity)

---

## 📈 Empirical Model Performance Benchmarks

Models were evaluated using a strict **Time-Aware Holdout Split**:
- **Training Set**: 1997–2015 (15,404 samples) with 5-Fold Cross-Validation.
- **Holdout Test Set**: 2016–2020 (4,285 samples).

| Model Architecture | 5-Fold CV $R^2$ | Test $R^2$ | Test RMSE (t/ha) | Test MAE (t/ha) | Generalization Verdict |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Linear Regression (Ridge)** | 0.5041 | 0.5966 | 540.75 | 43.48 | Baseline linear model |
| **Decision Tree Regressor** | 0.9664 | 0.9480 | 194.18 | 13.52 | Captures non-linear thresholds |
| **Random Forest Regressor** | **0.9157** | **0.9675** | **153.50** | **10.95** | **Selected Best Model** |
| **Gradient Boosting Regressor** | 0.9550 | 0.9497 | 190.97 | 13.85 | Strong ensemble boosting |

**Selected Model**: **Random Forest Regressor** minimized out-of-sample Test RMSE (153.50 t/ha) and Test MAE (10.95 t/ha) while yielding a Test $R^2$ of **0.9675**.

---

## 🚀 Setup & Execution Guide

### 1. Prerequisites & Environment Setup
Clone the repository and install required packages:
```bash
cd agriyield
pip install -r requirements.txt
```

### 2. Reproducing the End-to-End Pipeline
To run the automated data ingestion, cleaning, statistical analysis, and model training from scratch:
```bash
python src/data_loader.py
python src/preprocessing.py
python src/statistical_analysis.py
python src/train_models.py
python src/evaluate_models.py
```

### 3. Launching the Streamlit Web Application
Launch the interactive 8-page dashboard:
```bash
streamlit run app.py
```
The dashboard will open automatically in your browser at `http://localhost:8501`.

---

## 🔬 Core Academic Findings

1. **Biological Ceilings**: Crop genetic identity is the dominant determinant of yield variance ($H = 12,758.7$, $p < 0.001$), explaining $>70\%$ of model split importance.
2. **Simpson's Paradox**: In aggregate, chemical fertilizer intensity exhibits a weak monotonic correlation ($\rho = +0.02$). When stratified by crop species, high-biomass commercial crops (Sugarcane, Potato) show positive input responsiveness ($r = +0.173, +0.126$), whereas leguminous pulses exhibit flat/negative responsiveness.
3. **Precipitation Thresholds**: Yield displays diminishing marginal returns to annual precipitation; rainfall beyond 2,500 mm in waterlogged soils fails to improve cereal yields.

---

## ⚖️ Academic Disclaimer
**Correlation $\neq$ Causation**: Statistical co-movements and machine learning feature importances reflect predictive associations within historical census records. They do not constitute guaranteed causal agronomic prescriptions for field management.
