"""
AgriYield - Feature Engineering Module
Builds leakage-free agronomic features, handles log-transformations,
assembles Scikit-Learn preprocessing pipelines, and implements time-aware train/test splits.
"""

import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler, RobustScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

CLEANED_DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "cleaned_dataset.csv")


def engineer_agronomic_features(df):
    """
    Constructs agronomic ratio features and log transforms while strictly excluding Production
    to prevent target leakage.
    """
    data = df.copy()
    
    # 1. Intensity ratios
    data['Fertilizer_per_Area'] = data['Fertilizer'] / data['Area']
    data['Pesticide_per_Area'] = data['Pesticide'] / data['Area']
    
    # 2. Temporal feature
    data['Year_Index'] = data['Crop_Year'] - data['Crop_Year'].min()
    
    # 3. Log-transform highly skewed physical variables
    data['Log_Area'] = np.log1p(data['Area'])
    data['Log_Rainfall'] = np.log1p(data['Annual_Rainfall'])
    data['Log_Fertilizer_per_Area'] = np.log1p(data['Fertilizer_per_Area'])
    data['Log_Pesticide_per_Area'] = np.log1p(data['Pesticide_per_Area'])
    
    # Target variable check
    if 'Yield' in data.columns:
        # Guarantee non-negative
        data['Yield'] = np.clip(data['Yield'], a_min=0, a_max=None)
        
    return data


def get_feature_lists():
    """
    Returns lists of categorical and numerical predictor columns.
    Note: 'Production' is explicitly excluded.
    """
    categorical_features = ['Crop', 'State', 'Season']
    numerical_features = [
        'Crop_Year', 
        'Annual_Rainfall', 
        'Area', 
        'Fertilizer_per_Area', 
        'Pesticide_per_Area', 
        'Log_Area', 
        'Log_Rainfall',
        'Log_Fertilizer_per_Area',
        'Log_Pesticide_per_Area',
        'Year_Index'
    ]
    target_feature = 'Yield'
    
    return categorical_features, numerical_features, target_feature


def build_preprocessor():
    """
    Builds a Scikit-Learn ColumnTransformer for automated encoding and scaling.
    """
    cat_cols, num_cols, _ = get_feature_lists()
    
    cat_transformer = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
    num_transformer = RobustScaler()
    
    preprocessor = ColumnTransformer(
        transformers=[
            ('cat', cat_transformer, cat_cols),
            ('num', num_transformer, num_cols)
        ],
        remainder='drop'
    )
    return preprocessor


def split_data(df, split_method='time_aware', test_year_cutoff=2016, random_state=42):
    """
    Splits data into train and test sets.
    Methods:
    - 'time_aware': Train on years < test_year_cutoff (e.g. 1997-2015), test on >= cutoff (2016-2020)
    - 'random': Standard 80/20 train/test split with seed
    """
    df_feat = engineer_agronomic_features(df)
    cat_cols, num_cols, target = get_feature_lists()
    all_features = cat_cols + num_cols
    
    X = df_feat[all_features].copy()
    y = df_feat[target].copy()
    
    if split_method == 'time_aware' and 'Crop_Year' in df_feat.columns:
        train_mask = df_feat['Crop_Year'] < test_year_cutoff
        test_mask = df_feat['Crop_Year'] >= test_year_cutoff
        
        X_train, y_train = X[train_mask], y[train_mask]
        X_test, y_test = X[test_mask], y[test_mask]
        split_info = {
            "method": "Time-Aware Temporal Split",
            "train_period": f"1997 - {test_year_cutoff - 1}",
            "test_period": f"{test_year_cutoff} - 2020",
            "train_samples": len(X_train),
            "test_samples": len(X_test),
            "test_ratio": round(len(X_test) / len(X), 3)
        }
    else:
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=random_state, shuffle=True
        )
        split_info = {
            "method": "Random Stratified Split (80/20)",
            "train_samples": len(X_train),
            "test_samples": len(X_test),
            "test_ratio": 0.20
        }
        
    return X_train, X_test, y_train, y_test, split_info


def document_engineered_features():
    """
    Returns documentation of each engineered feature, formulas, and academic rationale.
    """
    return [
        {
            "Feature": "Fertilizer_per_Area",
            "Formula": "Fertilizer (kg) / Area (ha)",
            "Unit": "kg/ha",
            "Rationale": "Absolute fertilizer usage is proportional to farm size; application intensity per hectare measures true chemical input level."
        },
        {
            "Feature": "Pesticide_per_Area",
            "Formula": "Pesticide (kg) / Area (ha)",
            "Unit": "kg/ha",
            "Rationale": "Normalizes total pesticide consumption to per-hectare pest management pressure."
        },
        {
            "Feature": "Year_Index",
            "Formula": "Crop_Year - min(Crop_Year)",
            "Unit": "Years elapsed",
            "Rationale": "Captures multi-decade technological progress, farm mechanization, seed breeding innovations, and yield inflation."
        },
        {
            "Feature": "Log_Area",
            "Formula": "ln(1 + Area)",
            "Unit": "log(ha)",
            "Rationale": "Dampens extreme landholding scale variance across marginal farms vs large commercial estates."
        },
        {
            "Feature": "Log_Rainfall",
            "Formula": "ln(1 + Annual_Rainfall)",
            "Unit": "log(mm)",
            "Rationale": "Normalizes heavy right skew in monsoon precipitation across arid vs rainforest agro-climatic zones."
        },
        {
            "Feature": "Log_Fertilizer_per_Area",
            "Formula": "ln(1 + Fertilizer_per_Area)",
            "Unit": "log(kg/ha)",
            "Rationale": "Captures diminishing marginal returns of fertilizer according to Liebig's Law of the Minimum."
        }
    ]


if __name__ == "__main__":
    df = pd.read_csv(CLEANED_DATA_PATH)
    X_train, X_test, y_train, y_test, info = split_data(df, split_method='time_aware')
    print("Feature Engineering & Split Summary:")
    for k, v in info.items():
        print(f"  {k}: {v}")
    print("\nFeature matrix shape:", X_train.shape, "Target shape:", y_train.shape)
    print("\nEngineered Feature Documentation:")
    for doc in document_engineered_features()[:3]:
        print(f"  [{doc['Feature']}] {doc['Formula']} -> {doc['Rationale']}")
