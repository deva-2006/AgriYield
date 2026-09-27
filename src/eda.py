"""
AgriYield - Exploratory Data Analysis Module
Interactive Plotly visual generators for the 14 core agronomic and statistical charts.
Styled with a modern, high-contrast agricultural analytics palette.
"""

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Color Palette
AGRI_PALETTE = {
    "primary": "#10b981",       # Emerald green
    "secondary": "#059669",     # Deep emerald
    "accent": "#f59e0b",        # Golden amber
    "dark": "#0f172a",          # Deep slate
    "light": "#f8fafc",         # Crisp light background
    "neutral": "#64748b",       # Cool gray
    "warm": "#ef4444",          # Crimson
    "blue": "#0284c7"           # Sky blue
}

THEME_LAYOUT = dict(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(family="Plus Jakarta Sans, Inter, sans-serif", size=12, color="#cbd5e1"),
    margin=dict(l=40, r=40, t=50, b=40),
    hoverlabel=dict(bgcolor="#1e293b", font_size=12, font_color="#ffffff")
)


def plot_yield_distribution(df, log_scale=True):
    """
    Visualization 1: Target / Yield Distribution (Histogram + Boxplot).
    """
    data = df[df['Crop'] != 'Coconut'].copy() if 'Coconut' in df['Crop'].values else df.copy()
    
    fig = make_subplots(
        rows=2, cols=1,
        row_heights=[0.25, 0.75],
        shared_xaxes=True,
        vertical_spacing=0.05
    )
    
    # Boxplot on top
    fig.add_trace(
        go.Box(
            x=data['Yield'],
            name="Yield",
            marker_color=AGRI_PALETTE["secondary"],
            boxmean=True,
            orientation="h"
        ),
        row=1, col=1
    )
    
    # Histogram below
    fig.add_trace(
        go.Histogram(
            x=data['Yield'],
            nbinsx=60,
            marker_color=AGRI_PALETTE["primary"],
            opacity=0.85,
            name="Distribution"
        ),
        row=2, col=1
    )
    
    if log_scale:
        fig.update_xaxes(type="log", title_text="Crop Yield (Tonnes/Ha) [Log Scale]", row=2, col=1)
    else:
        fig.update_xaxes(title_text="Crop Yield (Tonnes/Ha)", row=2, col=1)
        
    fig.update_yaxes(title_text="Frequency", row=2, col=1)
    fig.update_layout(
        **THEME_LAYOUT,
        title="<b>Figure 4: Crop Yield Distribution</b> (with Central Tendency & Outliers)",
        showlegend=False,
        height=450
    )
    return fig


def plot_yield_by_crop(df, top_n=15):
    """
    Visualization 2: Yield by Crop (Top 15 and Bottom 15 crops).
    """
    data = df[df['Crop'] != 'Coconut'].copy() if 'Coconut' in df['Crop'].values else df.copy()
    crop_stats = data.groupby('Crop')['Yield'].agg(['mean', 'median', 'std', 'count']).reset_index()
    
    top_crops = crop_stats.sort_values('mean', ascending=False).head(top_n)
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=top_crops['mean'],
        y=top_crops['Crop'],
        orientation='h',
        marker=dict(
            color=top_crops['mean'],
            colorscale='Tealgrn',
            showscale=True,
            colorbar=dict(title="Tonnes/Ha")
        ),
        customdata=np.stack((top_crops['median'], top_crops['count']), axis=-1),
        hovertemplate="<b>%{y}</b><br>Mean Yield: %{x:.2f} t/ha<br>Median: %{customdata[0]:.2f} t/ha<br>Records: %{customdata[1]}<extra></extra>"
    ))
    
    fig.update_layout(
        **THEME_LAYOUT,
        title=f"<b>Figure 5: Mean Crop Yield by Species</b> (Top {top_n} Food & Cash Crops)",
        xaxis_title="Average Yield (Metric Tonnes / Hectare)",
        yaxis_title="",
        yaxis=dict(autorange="reversed"),
        height=500
    )
    return fig


def plot_yield_by_region(df, top_n=15):
    """
    Visualization 3: Yield by State / Region.
    """
    data = df[df['Crop'] != 'Coconut'].copy() if 'Coconut' in df['Crop'].values else df.copy()
    state_stats = data.groupby('State')['Yield'].agg(['mean', 'median', 'count']).reset_index()
    state_stats = state_stats.sort_values('mean', ascending=False).head(top_n)
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=state_stats['State'],
        y=state_stats['mean'],
        marker_color=AGRI_PALETTE["secondary"],
        text=[f"{v:.1f}" for v in state_stats['mean']],
        textposition="outside",
        hovertemplate="<b>%{x}</b><br>Mean Productivity: %{y:.2f} t/ha<extra></extra>"
    ))
    
    fig.update_layout(
        **THEME_LAYOUT,
        title=f"<b>Figure 6: Regional Yield Variance Across Indian States</b> (Top {top_n} Regions)",
        xaxis_title="State / Union Territory",
        yaxis_title="Average Yield (Tonnes / Ha)",
        xaxis_tickangle=-45,
        height=450
    )
    return fig


def plot_yield_over_time(df, selected_crops=None):
    """
    Visualization 4: Yield Over Time (Temporal Trends 1997-2020).
    """
    data = df[df['Crop'] != 'Coconut'].copy() if 'Coconut' in df['Crop'].values else df.copy()
    
    if selected_crops:
        data = data[data['Crop'].isin(selected_crops)]
    else:
        # Default top major crops
        top_crops = ['Rice', 'Wheat', 'Maize', 'Sugarcane', 'Potato']
        data = data[data['Crop'].isin(top_crops)]
        
    time_series = data.groupby(['Crop_Year', 'Crop'])['Yield'].mean().reset_index()
    
    fig = px.line(
        time_series,
        x='Crop_Year',
        y='Yield',
        color='Crop',
        markers=True,
        title="<b>Figure 7: Longitudinal Yield Trends (1997–2020)</b> by Major Crop Species",
        labels={"Crop_Year": "Harvest Year", "Yield": "Mean Yield (Tonnes/Ha)"},
        color_discrete_sequence=px.colors.qualitative.Dark24
    )
    
    fig.update_layout(
        **THEME_LAYOUT,
        hovermode="x unified",
        height=480
    )
    return fig


def plot_rainfall_distribution(df):
    """
    Visualization 5: Annual Rainfall Distribution.
    """
    fig = px.histogram(
        df,
        x='Annual_Rainfall',
        nbins=40,
        marginal='box',
        color_discrete_sequence=[AGRI_PALETTE["blue"]],
        title="<b>Figure 8a: Annual Rainfall Distribution (mm)</b> across Cultivation Regions",
        labels={'Annual_Rainfall': 'Annual Precipitation (mm)'}
    )
    fig.update_layout(**THEME_LAYOUT, height=420)
    return fig


def plot_fertilizer_distribution(df):
    """
    Visualization 6: Fertilizer Usage & Intensity Distribution.
    """
    data = df.copy()
    if 'Fertilizer_per_Area' not in data.columns:
        data['Fertilizer_per_Area'] = data['Fertilizer'] / data['Area']
        
    fig = px.histogram(
        data,
        x='Fertilizer_per_Area',
        nbins=50,
        marginal='box',
        color_discrete_sequence=[AGRI_PALETTE["primary"]],
        title="<b>Figure 8b: Fertilizer Application Intensity (kg/ha)</b>",
        labels={'Fertilizer_per_Area': 'Fertilizer Application Rate (kg/ha)'}
    )
    fig.update_xaxes(type="log", title_text="Fertilizer Intensity (kg/ha) [Log Scale]")
    fig.update_layout(**THEME_LAYOUT, height=420)
    return fig


def plot_pesticide_distribution(df):
    """
    Visualization 7: Pesticide Usage & Intensity Distribution.
    """
    data = df.copy()
    if 'Pesticide_per_Area' not in data.columns:
        data['Pesticide_per_Area'] = data['Pesticide'] / data['Area']
        
    fig = px.histogram(
        data,
        x='Pesticide_per_Area',
        nbins=50,
        marginal='box',
        color_discrete_sequence=[AGRI_PALETTE["accent"]],
        title="<b>Figure 8c: Pesticide Application Intensity (kg/ha)</b>",
        labels={'Pesticide_per_Area': 'Pesticide Application Rate (kg/ha)'}
    )
    fig.update_xaxes(type="log", title_text="Pesticide Intensity (kg/ha) [Log Scale]")
    fig.update_layout(**THEME_LAYOUT, height=420)
    return fig


def plot_rainfall_vs_yield(df, sample_size=2000):
    """
    Visualization 8: Annual Rainfall vs. Crop Yield.
    """
    data = df[df['Crop'] != 'Coconut'].copy() if 'Coconut' in df['Crop'].values else df.copy()
    if len(data) > sample_size:
        data = data.sample(sample_size, random_state=42)
        
    fig = px.scatter(
        data,
        x='Annual_Rainfall',
        y='Yield',
        color='Crop',
        opacity=0.6,
        trendline="ols",
        title="<b>Figure 8: Annual Rainfall vs. Crop Yield</b> (with OLS Trendline)",
        labels={'Annual_Rainfall': 'Precipitation (mm)', 'Yield': 'Yield (Tonnes/Ha)'},
        hover_data=['State', 'Crop_Year']
    )
    fig.update_yaxes(type="log", title_text="Crop Yield (Tonnes/Ha) [Log Scale]")
    fig.update_layout(**THEME_LAYOUT, height=500)
    return fig


def plot_fertilizer_vs_yield(df, sample_size=2000):
    """
    Visualization 9: Fertilizer Intensity vs. Crop Yield.
    """
    data = df[df['Crop'] != 'Coconut'].copy() if 'Coconut' in df['Crop'].values else df.copy()
    if 'Fertilizer_per_Area' not in data.columns:
        data['Fertilizer_per_Area'] = data['Fertilizer'] / data['Area']
        
    if len(data) > sample_size:
        data = data.sample(sample_size, random_state=42)
        
    fig = px.scatter(
        data,
        x='Fertilizer_per_Area',
        y='Yield',
        color='Crop',
        opacity=0.6,
        title="<b>Figure 9a: Fertilizer Application Rate vs. Crop Yield</b>",
        labels={'Fertilizer_per_Area': 'Fertilizer (kg/ha)', 'Yield': 'Yield (Tonnes/Ha)'},
        hover_data=['State', 'Crop_Year']
    )
    fig.update_xaxes(type="log", title_text="Fertilizer Rate (kg/ha) [Log Scale]")
    fig.update_yaxes(type="log", title_text="Crop Yield (Tonnes/Ha) [Log Scale]")
    fig.update_layout(**THEME_LAYOUT, height=500)
    return fig


def plot_pesticide_vs_yield(df, sample_size=2000):
    """
    Visualization 10: Pesticide Intensity vs. Crop Yield.
    """
    data = df[df['Crop'] != 'Coconut'].copy() if 'Coconut' in df['Crop'].values else df.copy()
    if 'Pesticide_per_Area' not in data.columns:
        data['Pesticide_per_Area'] = data['Pesticide'] / data['Area']
        
    if len(data) > sample_size:
        data = data.sample(sample_size, random_state=42)
        
    fig = px.scatter(
        data,
        x='Pesticide_per_Area',
        y='Yield',
        color='Crop',
        opacity=0.6,
        title="<b>Figure 9b: Pesticide Application Rate vs. Crop Yield</b>",
        labels={'Pesticide_per_Area': 'Pesticide (kg/ha)', 'Yield': 'Yield (Tonnes/Ha)'},
        hover_data=['State', 'Crop_Year']
    )
    fig.update_xaxes(type="log", title_text="Pesticide Rate (kg/ha) [Log Scale]")
    fig.update_yaxes(type="log", title_text="Crop Yield (Tonnes/Ha) [Log Scale]")
    fig.update_layout(**THEME_LAYOUT, height=500)
    return fig


def plot_area_vs_yield(df, sample_size=2000):
    """
    Visualization 11 & 12: Cultivated Land Area vs. Yield.
    """
    data = df[df['Crop'] != 'Coconut'].copy() if 'Coconut' in df['Crop'].values else df.copy()
    if len(data) > sample_size:
        data = data.sample(sample_size, random_state=42)
        
    fig = px.scatter(
        data,
        x='Area',
        y='Yield',
        color='Season',
        opacity=0.6,
        title="<b>Figure 9c: Sown Area vs. Crop Yield by Cropping Season</b>",
        labels={'Area': 'Cultivated Area (Hectares)', 'Yield': 'Yield (Tonnes/Ha)'},
        hover_data=['Crop', 'State']
    )
    fig.update_xaxes(type="log", title_text="Cultivated Area (Ha) [Log Scale]")
    fig.update_yaxes(type="log", title_text="Crop Yield (Tonnes/Ha) [Log Scale]")
    fig.update_layout(**THEME_LAYOUT, height=500)
    return fig


def plot_correlation_matrix(df, method='spearman'):
    """
    Visualization 13: Correlation Matrix Heatmap (Pearson or Spearman).
    """
    data = df[df['Crop'] != 'Coconut'].copy() if 'Coconut' in df['Crop'].values else df.copy()
    if 'Fertilizer_per_Area' not in data.columns:
        data['Fertilizer_per_Area'] = data['Fertilizer'] / data['Area']
    if 'Pesticide_per_Area' not in data.columns:
        data['Pesticide_per_Area'] = data['Pesticide'] / data['Area']
        
    num_cols = ['Yield', 'Annual_Rainfall', 'Area', 'Fertilizer_per_Area', 
                'Pesticide_per_Area', 'Crop_Year']
    existing_cols = [c for c in num_cols if c in data.columns]
    
    corr = data[existing_cols].corr(method=method).round(3)
    
    fig = px.imshow(
        corr,
        text_auto=True,
        aspect="auto",
        color_continuous_scale="RdBu_r",
        zmin=-1, zmax=1,
        title=f"<b>Figure 8: Pairwise Feature Correlation Matrix ({method.capitalize()})</b>"
    )
    fig.update_layout(**THEME_LAYOUT, height=480)
    return fig


def plot_pairwise_scatter_matrix(df, sample_size=1000):
    """
    Visualization 14: Pairwise Relationships for key numerical variables.
    """
    data = df[df['Crop'] != 'Coconut'].copy() if 'Coconut' in df['Crop'].values else df.copy()
    if 'Fertilizer_per_Area' not in data.columns:
        data['Fertilizer_per_Area'] = data['Fertilizer'] / data['Area']
    if 'Pesticide_per_Area' not in data.columns:
        data['Pesticide_per_Area'] = data['Pesticide'] / data['Area']
        
    if len(data) > sample_size:
        data = data.sample(sample_size, random_state=42)
        
    fig = px.scatter_matrix(
        data,
        dimensions=['Yield', 'Annual_Rainfall', 'Fertilizer_per_Area', 'Pesticide_per_Area'],
        color='Season',
        title="<b>Figure 9: Pairwise Feature Relationships Across Cropping Seasons</b>",
        labels={'Yield': 'Yield', 'Annual_Rainfall': 'Rainfall (mm)', 
                'Fertilizer_per_Area': 'Fert/Ha', 'Pesticide_per_Area': 'Pest/Ha'},
        height=650
    )
    fig.update_layout(**THEME_LAYOUT)
    return fig


if __name__ == "__main__":
    from preprocessing import CLEANED_DATASET_PATH
    df = pd.read_csv(CLEANED_DATASET_PATH)
    fig1 = plot_yield_distribution(df)
    fig2 = plot_yield_by_crop(df)
    fig13 = plot_correlation_matrix(df)
    print("EDA module loaded successfully and verified charts generation!")
