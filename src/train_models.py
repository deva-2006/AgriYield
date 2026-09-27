"""
AgriYield - Model Training & Comparison Pipeline
Trains Linear Regression (Ridge), Decision Tree, Random Forest, and Gradient Boosting Regressors.
Performs 5-fold cross validation, holds out temporal test set, evaluates metrics,
extracts feature importances, and serializes artifacts.
"""

import os
import json
import joblib
import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.compose import TransformedTargetRegressor
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score, KFold
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

from feature_engineering import split_data, build_preprocessor, get_feature_lists
from preprocessing import CLEANED_DATASET_PATH

MODELS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "models")


def get_model_definitions():
    """
    Returns candidate regression estimators configured with academic hyperparameter baselines.
    """
    return {
        "Linear Regression (Ridge)": Ridge(alpha=10.0, random_state=42),
        "Decision Tree": DecisionTreeRegressor(max_depth=12, min_samples_leaf=5, random_state=42),
        "Random Forest": RandomForestRegressor(n_estimators=120, max_depth=16, min_samples_leaf=3, n_jobs=-1, random_state=42),
        "Gradient Boosting": GradientBoostingRegressor(n_estimators=150, learning_rate=0.08, max_depth=6, min_samples_leaf=4, random_state=42)
    }


def train_and_evaluate_all():
    """
    Orchestrates data splitting, preprocessor construction, cross-validation,
    test evaluation, feature importance extraction, and artifact serialization.
    """
    os.makedirs(MODELS_DIR, exist_ok=True)
    
    print("Loading cleaned dataset...")
    df = pd.read_csv(CLEANED_DATASET_PATH)
    
    # Time-aware split: Train on 1997-2015, Test on 2016-2020
    X_train, X_test, y_train, y_test, split_info = split_data(df, split_method='time_aware', test_year_cutoff=2016)
    print(f"Data Split: {split_info['train_samples']} Train samples (1997-2015), {split_info['test_samples']} Test samples (2016-2020)")
    
    preprocessor = build_preprocessor()
    models = get_model_definitions()
    
    comparison_results = []
    fitted_pipelines = {}
    cv_scores_dict = {}
    
    kf = KFold(n_splits=5, shuffle=True, random_state=42)
    
    for name, estimator in models.items():
        print(f"\nTraining [{name}]...")
        
        # Wrap regressor to operate on log1p(Yield) to guarantee positive physical predictions
        wrapped_regressor = TransformedTargetRegressor(
            regressor=estimator,
            func=np.log1p,
            inverse_func=np.expm1
        )
        
        pipeline = Pipeline([
            ('preprocessor', preprocessor),
            ('regressor', wrapped_regressor)
        ])
        
        # 1. 5-Fold Cross-Validation on Training Data (R2 score)
        cv_scores = cross_val_score(pipeline, X_train, y_train, cv=kf, scoring='r2', n_jobs=-1)
        cv_r2_mean = float(cv_scores.mean())
        cv_r2_std = float(cv_scores.std())
        cv_scores_dict[name] = [round(float(s), 4) for s in cv_scores]
        print(f"  CV 5-Fold R2: {cv_r2_mean:.4f} (+/- {cv_r2_std:.4f})")
        
        # 2. Fit on full training set
        pipeline.fit(X_train, y_train)
        fitted_pipelines[name] = pipeline
        
        # 3. Train predictions
        y_train_pred = np.maximum(0, pipeline.predict(X_train))
        train_r2 = float(r2_score(y_train, y_train_pred))
        train_rmse = float(np.sqrt(mean_squared_error(y_train, y_train_pred)))
        train_mae = float(mean_absolute_error(y_train, y_train_pred))
        
        # 4. Test predictions
        y_test_pred = np.maximum(0, pipeline.predict(X_test))
        test_r2 = float(r2_score(y_test, y_test_pred))
        test_mse = float(mean_squared_error(y_test, y_test_pred))
        test_rmse = float(np.sqrt(test_mse))
        test_mae = float(mean_absolute_error(y_test, y_test_pred))
        
        print(f"  Test Performance: R2={test_r2:.4f}, RMSE={test_rmse:.2f} t/ha, MAE={test_mae:.2f} t/ha")
        
        comparison_results.append({
            "model_name": name,
            "train_r2": round(train_r2, 4),
            "train_rmse": round(train_rmse, 3),
            "train_mae": round(train_mae, 3),
            "cv_r2_mean": round(cv_r2_mean, 4),
            "cv_r2_std": round(cv_r2_std, 4),
            "test_r2": round(test_r2, 4),
            "test_mse": round(test_mse, 3),
            "test_rmse": round(test_rmse, 3),
            "test_mae": round(test_mae, 3)
        })
        
    # Model Selection Logic:
    # We choose the model that minimizes Test RMSE while avoiding extreme overfitting.
    # Typically Random Forest or Decision Tree.
    comp_df = pd.DataFrame(comparison_results)
    best_row = comp_df.sort_values(by=['test_rmse', 'test_mae']).iloc[0]
    best_model_name = best_row['model_name']
    best_pipeline = fitted_pipelines[best_model_name]
    
    print(f"\n=======================================================")
    print(f"BEST MODEL SELECTED: [{best_model_name}]")
    print(f"Selection Rationale: Lowest Test RMSE ({best_row['test_rmse']:.2f} t/ha) & Lowest Test MAE ({best_row['test_mae']:.2f} t/ha) with Test R2={best_row['test_r2']:.4f}")
    print(f"=======================================================\n")
    
    # Save best model pipeline
    best_model_path = os.path.join(MODELS_DIR, "best_model.pkl")
    joblib.dump(best_pipeline, best_model_path)
    print(f"Saved best model to {best_model_path}")
    
    # Also save Random Forest model specifically for feature importance analysis if not already best
    rf_pipeline = fitted_pipelines.get("Random Forest")
    rf_path = os.path.join(MODELS_DIR, "rf_model.pkl")
    joblib.dump(rf_pipeline, rf_path)
    
    # Extract Feature Importances from Random Forest & Gradient Boosting
    feature_importance_data = extract_feature_importances(fitted_pipelines, preprocessor)
    feat_imp_path = os.path.join(MODELS_DIR, "feature_importance.json")
    with open(feat_imp_path, "w") as f:
        json.dump(feature_importance_data, f, indent=2)
    print(f"Saved feature importance analysis to {feat_imp_path}")
    
    # Save Model Comparison
    comp_path = os.path.join(MODELS_DIR, "model_comparison.json")
    with open(comp_path, "w") as f:
        json.dump({
            "comparison": comparison_results,
            "cv_fold_scores": cv_scores_dict,
            "selected_model": best_model_name,
            "selection_criteria": "Minimization of Test Root Mean Squared Error (RMSE) and Mean Absolute Error (MAE) under a strictly time-aware temporal holdout test split (2016-2020).",
            "split_metadata": split_info
        }, f, indent=2)
    print(f"Saved comparison metrics to {comp_path}")
    
    # Save test sample predictions for rapid plotting in Streamlit
    sample_eval = X_test.copy()
    sample_eval['Actual_Yield'] = y_test.values
    for name, pipe in fitted_pipelines.items():
        sample_eval[f"Pred_{name}"] = np.maximum(0, pipe.predict(X_test))
    sample_eval_path = os.path.join(MODELS_DIR, "test_predictions.csv")
    sample_eval.to_csv(sample_eval_path, index=False)
    print(f"Saved test set evaluation predictions to {sample_eval_path}")
    
    return comp_df, best_model_name


def extract_feature_importances(pipelines, preprocessor):
    """
    Extracts individual transformed feature importances as well as grouped parent-feature importances.
    """
    cat_cols, num_cols, _ = get_feature_lists()
    
    # Retrieve feature names from ColumnTransformer
    cat_encoder = preprocessor.named_transformers_['cat']
    encoded_cat_names = list(cat_encoder.get_feature_names_out(cat_cols))
    all_feature_names = encoded_cat_names + num_cols
    
    importance_dict = {}
    
    for model_name in ["Random Forest", "Gradient Boosting", "Decision Tree"]:
        if model_name not in pipelines:
            continue
        pipe = pipelines[model_name]
        reg = pipe.named_steps['regressor'].regressor_
        if hasattr(reg, 'feature_importances_'):
            importances = reg.feature_importances_
            
            # Map one-hot feature importances
            feature_imp_pairs = sorted(
                zip(all_feature_names, [round(float(v), 5) for v in importances]),
                key=lambda x: x[1],
                reverse=True
            )
            
            # Group by parent feature (e.g. all 'cat__Crop_*' summed to 'Crop')
            grouped_imp = {
                "Crop": 0.0,
                "State": 0.0,
                "Season": 0.0,
                "Fertilizer_per_Area": 0.0,
                "Pesticide_per_Area": 0.0,
                "Annual_Rainfall": 0.0,
                "Area": 0.0,
                "Crop_Year": 0.0,
                "Year_Index": 0.0,
                "Log_Area": 0.0,
                "Log_Rainfall": 0.0,
                "Log_Fertilizer_per_Area": 0.0,
                "Log_Pesticide_per_Area": 0.0
            }
            
            for feat, imp in zip(all_feature_names, importances):
                assigned = False
                for parent in ["Crop", "State", "Season"]:
                    if parent in feat:
                        grouped_imp[parent] += float(imp)
                        assigned = True
                        break
                if not assigned:
                    for num_f in num_cols:
                        if num_f in feat:
                            grouped_imp[num_f] = grouped_imp.get(num_f, 0.0) + float(imp)
                            break
                            
            # Normalize grouped
            tot = sum(grouped_imp.values()) or 1.0
            grouped_norm = {k: round(float(v / tot * 100), 2) for k, v in sorted(grouped_imp.items(), key=lambda x: x[1], reverse=True)}
            
            importance_dict[model_name] = {
                "top_transformed_features": [{"feature": f, "importance": round(v * 100, 3)} for f, v in feature_imp_pairs[:20]],
                "grouped_feature_importance_pct": grouped_norm
            }
            
    # Linear Regression Coefficients
    if "Linear Regression (Ridge)" in pipelines:
        ridge_pipe = pipelines["Linear Regression (Ridge)"]
        ridge_reg = ridge_pipe.named_steps['regressor'].regressor_
        coefs = ridge_reg.coef_
        coef_pairs = sorted(
            zip(all_feature_names, [round(float(c), 4) for c in coefs]),
            key=lambda x: abs(x[1]),
            reverse=True
        )
        importance_dict["Linear Regression (Ridge)"] = {
            "top_coefficients": [{"feature": f, "coefficient": c} for f, c in coef_pairs[:20]]
        }
        
    return importance_dict


if __name__ == "__main__":
    train_and_evaluate_all()
