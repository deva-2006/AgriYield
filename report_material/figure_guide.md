# AgriYield: Internship Report Figure Reference Guide

This guide details the thirteen essential figures to capture from the **AgriYield** project for inclusion in an academic thesis or internship report. Each figure entry outlines its academic purpose, what it demonstrates, and the exact navigation location within the dashboard or codebase.

---

### Figure 1 — Overall Data Science Workflow
- **Title**: *End-to-End Data Science Architecture for AgriYield*
- **Source Location**: Dashboard $\to$ **Methodology Page** (Top visual workflow diagram) or `report_material/methodology.md`.
- **What it Demonstrates**: Illustrates the complete 11-stage pipeline: Data Ingestion $\to$ Quality Audit $\to$ Reproducible Cleaning $\to$ Exploratory Data Analysis $\to$ Hypothesis Testing $\to$ Leakage-Free Feature Engineering $\to$ Temporal Train/Test Split $\to$ Model Training $\to$ Model Evaluation $\to$ Model Interpretation $\to$ Real-Time Prediction.

---

### Figure 2 — Dataset Structure & Attribute Schema
- **Title**: *Longitudinal Census Schema and Variable Definitions*
- **Source Location**: Dashboard $\to$ **Dataset Explorer Page** $\to$ *Column Metadata* tab.
- **What it Demonstrates**: Presents the 10 core attributes (`Crop`, `Crop_Year`, `Season`, `State`, `Area`, `Production`, `Annual_Rainfall`, `Fertilizer`, `Pesticide`, `Yield`), their verified data types, and physical units ($\text{t/ha}$, $\text{mm}$, $\text{kg/ha}$).

---

### Figure 3 — Data Quality & Missing Value Audit Scorecard
- **Title**: *Data Completeness and Integrity Verification*
- **Source Location**: Dashboard $\to$ **Dataset Explorer Page** $\to$ *Quality Audit* tab.
- **What it Demonstrates**: Validates the 100.0% data completeness metric (0 missing cells out of 196,890 total entries, 0 duplicate records), confirming data integrity prior to modeling.

---

### Figure 4 — Crop Yield Distribution
- **Title**: *Longitudinal Crop Yield Distribution and Boxplot*
- **Source Location**: Dashboard $\to$ **Exploratory Analysis Page** $\to$ *Distributions & Outliers* tab (Figure 4).
- **What it Demonstrates**: Highlights the severe positive right-skewness of raw crop yields (skewness $= 18.2$, kurtosis $= 364.5$). Shows median productivity at ~1.03 t/ha alongside the long tail formed by high-biomass cash crops (Sugarcane, Potato).

---

### Figure 5 — Crop-wise Yield Analysis
- **Title**: *Mean Productivity Across Major Food and Commercial Crops*
- **Source Location**: Dashboard $\to$ **Exploratory Analysis Page** $\to$ *Crop & Regional Variance* tab (Figure 5).
- **What it Demonstrates**: Contrasts biomass production across species: perennial Sugarcane ($51.73$ t/ha) and tubers ($13.33$ t/ha) vs. cereal grains ($2.5–3.5$ t/ha) and protein-dense pulses ($0.4–0.9$ t/ha).

---

### Figure 6 — Regional Yield Analysis Across Indian States
- **Title**: *Regional Yield Heterogeneity Across Indian States*
- **Source Location**: Dashboard $\to$ **Exploratory Analysis Page** $\to$ *Crop & Regional Variance* tab (Figure 6).
- **What it Demonstrates**: Depicts state-level productivity disparities. Irrigated Indo-Gangetic and coastal delta states (Punjab $4.2$ t/ha, Tamil Nadu $3.9$ t/ha) lead national output, while rainfed central plateau regions report lower averages.

---

### Figure 7 — Longitudinal Yield Trends (1997–2020)
- **Title**: *Long-Term Yield Trajectories and Climate Shock Dips*
- **Source Location**: Dashboard $\to$ **Exploratory Analysis Page** $\to$ *Longitudinal Trends* tab (Figure 7).
- **What it Demonstrates**: Displays multi-decade productivity improvements alongside pronounced downward spikes in 2002, 2009, and 2014–2015, directly coinciding with historical El Niño drought events.

---

### Figure 8 — Environmental & Input Correlation Matrix
- **Title**: *Pairwise Spearman Correlation Matrix Across Agro-Climatic Features*
- **Source Location**: Dashboard $\to$ **Exploratory Analysis Page** $\to$ *Climate & Inputs vs. Yield* tab (Figure 8).
- **What it Demonstrates**: Shows correlation coefficients between yield, rainfall, land area, and input application intensities. Highlights weak aggregate correlations that motivate non-linear ensemble modeling.

---

### Figure 9 — Bivariate Feature Relationships & Input Curves
- **Title**: *Bivariate Scatter Plots of Precipitation and Fertilizer Intensities vs. Yield*
- **Source Location**: Dashboard $\to$ **Exploratory Analysis Page** $\to$ *Climate & Inputs vs. Yield* tab (Figure 9a/b).
- **What it Demonstrates**: Illustrates non-linear diminishing returns (Liebig's Law) and saturation effects on log-log scales, demonstrating that chemical inputs plateau in productivity benefits.

---

### Figure 10 — Model Performance Benchmark Comparison
- **Title**: *Comparison of Train R², 5-Fold Cross-Validation R², and Holdout Test R²*
- **Source Location**: Dashboard $\to$ **Model Evaluation Page** (Figure 10).
- **What it Demonstrates**: Benchmarks Linear Regression (Ridge), Decision Tree, Random Forest, and Gradient Boosting. Demonstrates Random Forest's superior generalizability (Test $R^2 = 0.9675$, Test RMSE $= 153.50$ t/ha).

---

### Figure 11 — Actual vs. Predicted Yield Diagnostics
- **Title**: *Actual vs. Predicted Yield on Holdout Test Set (2016–2020)*
- **Source Location**: Dashboard $\to$ **Model Evaluation Page** (Figure 11).
- **What it Demonstrates**: Scatter plot comparing observed versus predicted yields with the red 45-degree identity diagonal ($y = x$). Points closely hug the diagonal across five orders of magnitude, verifying model precision.

---

### Figure 12 — Grouped Feature Importance Architecture
- **Title**: *Hierarchical Feature Importance in Crop Yield Prediction*
- **Source Location**: Dashboard $\to$ **Feature Importance Page** (Figure 12).
- **What it Demonstrates**: Deconstructs predictive contributions: Crop biological identity accounts for $71.8\%$ of split decisions, State geography for $11.4\%$, and fertilizer intensity for $6.1\%$.

---

### Figure 13 — Interactive Yield Prediction Dashboard
- **Title**: *AgriYield Real-Time Simulation and Decision Support Interface*
- **Source Location**: Dashboard $\to$ **Yield Prediction Page**.
- **What it Demonstrates**: Captures the operational inference simulator displaying user input parameters, the predicted point yield ($3.00$ t/ha for Punjab Wheat), 90% confidence interval, estimated total production, and model context.
