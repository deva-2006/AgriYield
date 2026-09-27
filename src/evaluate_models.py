"""
AgriYield - Model Evaluation & Diagnostics Module
Generates diagnostic visual plots: Actual vs. Predicted, Residuals vs. Fitted,
Residual Error Distribution, and Cross-Model Comparison Charts.
"""

import os
import json
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from eda import THEME_LAYOUT, AGRI_PALETTE

MODELS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "models")
COMPARISON_JSON_PATH = os.path.join(MODELS_DIR, "model_comparison.json")
TEST_PREDICTIONS_PATH = os.path.join(MODELS_DIR, "test_predictions.csv")


def load_evaluation_data():
    """Loads saved model comparison metrics and test evaluation predictions."""
    comp_data = {}
    if os.path.exists(COMPARISON_JSON_PATH):
        with open(COMPARISON_JSON_PATH, "r") as f:
            comp_data = json.load(f)
            
    test_preds_df = pd.DataFrame()
    if os.path.exists(TEST_PREDICTIONS_PATH):
        test_preds_df = pd.read_csv(TEST_PREDICTIONS_PATH)
        
    return comp_data, test_preds_df


def plot_model_comparison_metrics(comp_data):
    """
    Visualization 10: Model Comparison Chart across Train R2, CV R2, and Test R2.
    """
    comp_list = comp_data.get("comparison", [])
    if not comp_list:
        return go.Figure()
        
    df = pd.DataFrame(comp_list)
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=df['model_name'],
        y=df['train_r2'],
        name="Train R²",
        marker_color="#94a3b8"
    ))
    fig.add_trace(go.Bar(
        x=df['model_name'],
        y=df['cv_r2_mean'],
        name="5-Fold CV R²",
        marker_color=AGRI_PALETTE["accent"]
    ))
    fig.add_trace(go.Bar(
        x=df['model_name'],
        y=df['test_r2'],
        name="Holdout Test R²",
        marker_color=AGRI_PALETTE["primary"]
    ))
    
    fig.update_layout(
        **THEME_LAYOUT,
        barmode='group',
        title="<b>Figure 10: Model Performance Comparison</b> (Train vs. 5-Fold CV vs. Test R²)",
        yaxis_title="R² Determination Coefficient",
        xaxis_title="",
        yaxis=dict(range=[0, 1.05]),
        height=450
    )
    return fig


def plot_actual_vs_predicted(test_preds_df, model_name="Random Forest", sample_size=1500):
    """
    Visualization 11: Actual vs. Predicted Crop Yield with Identity Line (y = x).
    """
    col = f"Pred_{model_name}"
    if col not in test_preds_df.columns:
        # Fallback to first pred column
        pred_cols = [c for c in test_preds_df.columns if c.startswith("Pred_")]
        if not pred_cols:
            return go.Figure()
        col = pred_cols[0]
        model_name = col.replace("Pred_", "")
        
    df_plot = test_preds_df.dropna(subset=['Actual_Yield', col]).copy()
    if len(df_plot) > sample_size:
        df_plot = df_plot.sample(sample_size, random_state=42)
        
    fig = px.scatter(
        df_plot,
        x='Actual_Yield',
        y=col,
        color='Crop' if 'Crop' in df_plot.columns else None,
        opacity=0.65,
        title=f"<b>Figure 11: Actual vs. Predicted Yield — {model_name}</b> (Holdout 2016–2020)",
        labels={'Actual_Yield': 'Actual Yield (Tonnes/Ha)', col: 'Predicted Yield (Tonnes/Ha)'},
        hover_data=['State', 'Crop_Year'] if 'State' in df_plot.columns else None
    )
    
    # 45-degree reference line
    max_val = max(df_plot['Actual_Yield'].max(), df_plot[col].max())
    fig.add_trace(go.Scatter(
        x=[0.1, max_val],
        y=[0.1, max_val],
        mode='lines',
        line=dict(color='#ef4444', dash='dash', width=2),
        name='Ideal Identity (y = x)'
    ))
    
    fig.update_xaxes(type="log", title_text="Actual Yield (Tonnes/Ha) [Log Scale]")
    fig.update_yaxes(type="log", title_text="Predicted Yield (Tonnes/Ha) [Log Scale]")
    fig.update_layout(**THEME_LAYOUT, height=520)
    return fig


def plot_residual_analysis(test_preds_df, model_name="Random Forest", sample_size=1500):
    """
    Residual Plot: Residuals (Actual - Predicted) vs. Predicted Yield.
    """
    col = f"Pred_{model_name}"
    if col not in test_preds_df.columns:
        return go.Figure()
        
    df_plot = test_preds_df.dropna(subset=['Actual_Yield', col]).copy()
    df_plot['Residual'] = df_plot['Actual_Yield'] - df_plot[col]
    
    if len(df_plot) > sample_size:
        df_plot = df_plot.sample(sample_size, random_state=42)
        
    fig = px.scatter(
        df_plot,
        x=col,
        y='Residual',
        color='Crop' if 'Crop' in df_plot.columns else None,
        opacity=0.6,
        title=f"<b>Residual Diagnostics for {model_name}</b> (Residuals vs. Fitted)",
        labels={col: 'Predicted Yield (Tonnes/Ha)', 'Residual': 'Residual Error (Actual - Pred)'}
    )
    
    # Zero error line
    fig.add_hline(y=0, line_dash="dash", line_color="#ef4444", annotation_text="Zero Residual Line")
    fig.update_xaxes(type="log", title_text="Predicted Yield (Tonnes/Ha) [Log Scale]")
    fig.update_layout(**THEME_LAYOUT, height=480)
    return fig


def plot_error_distribution(test_preds_df, model_name="Random Forest"):
    """
    Error Distribution: Histogram of Residuals.
    """
    col = f"Pred_{model_name}"
    if col not in test_preds_df.columns:
        return go.Figure()
        
    residuals = test_preds_df['Actual_Yield'] - test_preds_df[col]
    
    # Filter extreme outliers for clear visualization
    q01 = residuals.quantile(0.01)
    q99 = residuals.quantile(0.99)
    res_trimmed = residuals[(residuals >= q01) & (residuals <= q99)]
    
    fig = px.histogram(
        x=res_trimmed,
        nbins=60,
        marginal='box',
        color_discrete_sequence=[AGRI_PALETTE["primary"]],
        title=f"<b>Residual Error Distribution for {model_name}</b> (Trimmed 1st-99th percentile)",
        labels={'x': 'Prediction Error (Actual - Predicted) [Tonnes/Ha]'}
    )
    fig.update_layout(**THEME_LAYOUT, height=450)
    return fig


if __name__ == "__main__":
    comp, preds = load_evaluation_data()
    print("Loaded evaluation data:")
    print("Comparison models:", [m['model_name'] for m in comp.get('comparison', [])])
    print("Test predictions shape:", preds.shape)
    fig = plot_model_comparison_metrics(comp)
    print("Generated model comparison plot successfully!")
