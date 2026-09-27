"""
AgriYield - Data Loader and Understanding Module
Handles dataset ingestion, structural auditing, quality assessments, and descriptive stats.
"""

import os
import pandas as pd
import numpy as np

DATASET_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "dataset.csv")
DATASET_URL = "https://raw.githubusercontent.com/Aswins10/Agricultural-Crop-Yield-in-Indian-States-Dataset/main/crop_yield.csv"


def get_dataset_metadata():
    """
    Returns verified academic metadata regarding the dataset provenance,
    schema, target variable, and constraints.
    """
    return {
        "dataset_name": "Agricultural Crop Yield in Indian States Dataset (1997-2020)",
        "source": "Directorate of Economics and Statistics (DES), Ministry of Agriculture and Farmers Welfare & India Meteorological Department (IMD)",
        "source_url": DATASET_URL,
        "citation": "Government of India Open Government Data (OGD) Platform & Kaggle Agricultural Repository",
        "target_variable": "Yield",
        "target_units": "Metric Tonnes per Hectare (Tonnes/Ha) for field crops; Nuts per Hectare for Coconut",
        "number_of_records": 19689,
        "number_of_columns": 10,
        "features": {
            "Crop": "Specific crop cultivated (55 distinct species across cereals, pulses, oilseeds, cash crops)",
            "Crop_Year": "Agricultural harvest year (1997 - 2020)",
            "Season": "Agricultural cropping season (Kharif, Rabi, Whole Year, Summer, Autumn, Winter)",
            "State": "Indian State / Union Territory where cultivation occurred (30 administrative regions)",
            "Area": "Total land area sown under the crop in Hectares (Ha)",
            "Production": "Total harvest output in Metric Tonnes (except Coconut, which is enumerated in thousands of nuts)",
            "Annual_Rainfall": "Total annual precipitation received in millimeters (mm)",
            "Fertilizer": "Total chemical fertilizer consumed in kilograms (kg)",
            "Pesticide": "Total pesticide applied in kilograms (kg)",
            "Yield": "Productivity metric defined as Production / Area (Tonnes/Ha)"
        },
        "limitations": [
            "Meteorological data represents state-wide annual aggregate precipitation rather than micro-climatic or seasonal growth stage rainfall.",
            "Soil chemical profiles (N-P-K, pH, organic carbon) and irrigation percentages are not directly recorded in this nationwide census series.",
            "Coconut records employ a distinct unit scale (nuts instead of metric tonnes), requiring specific domain handling."
        ]
    }


def load_raw_data(filepath=None):
    """
    Loads raw CSV data. If not present locally, attempts download from URL.
    """
    path = filepath or DATASET_PATH
    if not os.path.exists(path):
        import urllib.request
        os.makedirs(os.path.dirname(path), exist_ok=True)
        print(f"Downloading dataset from {DATASET_URL}...")
        req = urllib.request.Request(DATASET_URL, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as resp, open(path, 'wb') as f:
            f.write(resp.read())
        print(f"Saved dataset to {path}")
    
    df = pd.read_csv(path)
    return df


def audit_dataset(df):
    """
    Performs complete automated data audit:
    - Shape, types, missing values, duplicates, unique values
    - Numerical distributions (mean, std, min, quartiles, max, skewness, kurtosis)
    - Categorical value counts
    - Data quality summary
    """
    num_rows, num_cols = df.shape
    missing_counts = df.isnull().sum().to_dict()
    missing_pct = (df.isnull().sum() / num_rows * 100).to_dict()
    duplicate_rows = int(df.duplicated().sum())
    
    dtypes = {col: str(dtype) for col, dtype in df.dtypes.items()}
    unique_counts = {col: int(df[col].nunique()) for col in df.columns}
    
    num_cols_list = df.select_dtypes(include=[np.number]).columns.tolist()
    cat_cols_list = df.select_dtypes(include=['object']).columns.tolist()
    
    # Descriptive numerical statistics with skewness & kurtosis
    num_stats = {}
    for col in num_cols_list:
        series = df[col].dropna()
        num_stats[col] = {
            "count": int(series.count()),
            "mean": float(series.mean()),
            "std": float(series.std()),
            "min": float(series.min()),
            "25%": float(series.quantile(0.25)),
            "50%": float(series.median()),
            "75%": float(series.quantile(0.75)),
            "max": float(series.max()),
            "skewness": float(series.skew()),
            "kurtosis": float(series.kurtosis())
        }
        
    # Categorical distributions
    cat_stats = {}
    for col in cat_cols_list:
        counts = df[col].value_counts().head(10).to_dict()
        cat_stats[col] = {
            "top_categories": {str(k): int(v) for k, v in counts.items()},
            "unique_total": int(df[col].nunique())
        }
        
    # Quality flags
    zero_yield_count = int((df['Yield'] == 0).sum()) if 'Yield' in df.columns else 0
    
    quality_summary = {
        "total_records": num_rows,
        "total_attributes": num_cols,
        "duplicate_records": duplicate_rows,
        "has_missing_values": sum(missing_counts.values()) > 0,
        "total_missing_cells": int(sum(missing_counts.values())),
        "zero_yield_records": zero_yield_count,
        "data_completeness_pct": float(100.0 - (sum(missing_counts.values()) / (num_rows * num_cols) * 100))
    }
    
    return {
        "metadata": get_dataset_metadata(),
        "shape": (num_rows, num_cols),
        "data_types": dtypes,
        "missing_counts": missing_counts,
        "missing_percentages": missing_pct,
        "duplicate_rows": duplicate_rows,
        "unique_counts": unique_counts,
        "numerical_statistics": num_stats,
        "categorical_statistics": cat_stats,
        "quality_summary": quality_summary
    }


if __name__ == "__main__":
    df = load_raw_data()
    print("Dataset loaded successfully!")
    audit = audit_dataset(df)
    print("\n--- Data Quality Audit Summary ---")
    for k, v in audit["quality_summary"].items():
        print(f"  {k}: {v}")
    print("\n--- Numerical Summary (Sample Columns) ---")
    for col in ["Yield", "Annual_Rainfall", "Fertilizer", "Pesticide"]:
        s = audit["numerical_statistics"][col]
        print(f"  {col}: Mean={s['mean']:.2f}, Std={s['std']:.2f}, Min={s['min']}, Median={s['50%']:.2f}, Max={s['max']:.2f}")
