"""
AgriYield - Data Science-Based Crop Yield Analysis and Prediction
Executive Presentation Dashboard
"""

import os
import sys
import json
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

# Add src to system path
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from data_loader import load_raw_data, audit_dataset
from preprocessing import CLEANED_DATASET_PATH, clean_crop_data
from eda import THEME_LAYOUT, AGRI_PALETTE
from evaluate_models import load_evaluation_data
from prediction import predict_crop_yield

# ---------------------------------------------------------
# Page Configuration & Executive Presentation Styling
# ---------------------------------------------------------
st.set_page_config(
    page_title="AgriYield — Crop Yield Analysis & Prediction",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

CUSTOM_CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    /* Top Hero Header */
    .hero-banner {
        background: linear-gradient(135deg, #064e3b 0%, #065f46 50%, #047857 100%);
        border: 1px solid rgba(16, 185, 129, 0.3);
        border-radius: 16px;
        padding: 2rem 2.5rem;
        color: white;
        margin-bottom: 1.8rem;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.25);
    }
    .hero-banner h1 {
        font-size: 2.2rem;
        font-weight: 800;
        margin: 0 0 0.4rem 0;
        color: #f0fdf4 !important;
        letter-spacing: -0.02em;
    }
    .hero-banner p {
        font-size: 1.05rem;
        margin: 0;
        color: #a7f3d0 !important;
        opacity: 0.95;
    }
    
    /* Metric Badge Pills */
    .badge-container {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin-top: 1rem;
    }
    .badge-pill {
        background: rgba(255, 255, 255, 0.12);
        border: 1px solid rgba(255, 255, 255, 0.25);
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
        color: #ecfdf5 !important;
    }
    
    /* Adaptive Sleek Cards */
    .card {
        background-color: var(--secondary-background-color, #182234);
        border: 1px solid rgba(148, 163, 184, 0.18);
        border-radius: 12px;
        padding: 1.4rem;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        margin-bottom: 1.2rem;
        color: var(--text-color, #f1f5f9);
    }
    .card h3, .card h4 {
        color: #10b981 !important;
        margin-top: 0;
        font-weight: 700;
    }
    .card p, .card li, .card span {
        color: var(--text-color, #cbd5e1);
        line-height: 1.6;
    }
    .card b, .card strong {
        color: var(--text-color, #f8fafc);
        font-weight: 700;
    }
    
    /* Adaptive Sleek Metric Boxes */
    .metric-box {
        background-color: var(--secondary-background-color, #182234);
        border: 1px solid rgba(148, 163, 184, 0.18);
        border-radius: 12px;
        padding: 1.3rem 1.4rem;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        border-top: 4px solid #10b981;
        color: var(--text-color, #f1f5f9);
    }
    .metric-label {
        font-size: 0.82rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #94a3b8;
        margin-bottom: 0.3rem;
    }
    .metric-val {
        font-size: 1.9rem;
        font-weight: 800;
        color: #10b981;
        line-height: 1.1;
    }
    .metric-sub {
        font-size: 0.82rem;
        color: #94a3b8;
        margin-top: 0.4rem;
        line-height: 1.4;
    }
    .metric-sub b, .metric-sub strong {
        color: var(--text-color, #f8fafc);
    }
    
    /* Harvest Summary Card */
    .summary-box {
        background: rgba(16, 185, 129, 0.12);
        border: 1px solid rgba(16, 185, 129, 0.3);
        border-left: 6px solid #10b981;
        border-radius: 12px;
        padding: 1.2rem 1.6rem;
        margin-bottom: 1.5rem;
        color: var(--text-color, #f1f5f9);
    }
    .summary-box h3 {
        color: #10b981 !important;
        margin: 0 0 0.4rem 0;
        font-size: 1.25rem;
        font-weight: 700;
    }
    .summary-box p {
        font-size: 1.02rem;
        line-height: 1.6;
        margin: 0;
        color: var(--text-color, #f1f5f9);
    }
    .summary-box b, .summary-box strong {
        color: #34d399 !important;
    }
    
    /* Professional Analytical Insight Box */
    .insight-card {
        background: rgba(16, 185, 129, 0.08);
        border-left: 4px solid #10b981;
        border-top: 1px solid rgba(16, 185, 129, 0.2);
        border-right: 1px solid rgba(16, 185, 129, 0.2);
        border-bottom: 1px solid rgba(16, 185, 129, 0.2);
        padding: 1rem 1.4rem;
        border-radius: 0 10px 10px 0;
        margin: 0.9rem 0 1.2rem 0;
        font-size: 0.94rem;
        color: var(--text-color, #f1f5f9);
    }
    .insight-card strong, .insight-card b {
        color: #34d399 !important;
    }
    
    /* Scenario Selector Header */
    .preset-title {
        font-size: 0.85rem;
        font-weight: 700;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 0.5rem;
    }

    /* Light Mode Overrides */
    @media (prefers-color-scheme: light) {
        .card b, .card strong, .metric-sub b, .metric-sub strong {
            color: #0f172a !important;
        }
        .insight-card strong, .insight-card b, .summary-box b, .summary-box strong {
            color: #065f46 !important;
        }
        .insight-card {
            background: #f0fdf4;
            color: #1e293b;
        }
        .summary-box {
            background: #f0fdf4;
            color: #1e293b;
        }
    }
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


# ---------------------------------------------------------
# Cached Data Loader
# ---------------------------------------------------------
@st.cache_data
def get_dataset():
    if os.path.exists(CLEANED_DATASET_PATH):
        return pd.read_csv(CLEANED_DATASET_PATH)
    raw = load_raw_data()
    clean_df, _ = clean_crop_data(raw)
    return clean_df


df = get_dataset()
comp_data, test_preds = load_evaluation_data()

# ---------------------------------------------------------
# Sidebar Navigation
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h2 style='color:#10b981; margin:0 0 0.2rem 0; font-weight:800;'>🌾 AgriYield</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#94a3b8; font-size:0.85rem; margin:0 0 1.2rem 0;'>Data Science Crop Yield Platform</p>", unsafe_allow_html=True)
    
    section = st.radio(
        "Navigation",
        [
            "🎯 Project Overview",
            "🔮 Live Prediction Simulator",
            "📊 Core Agricultural Insights",
            "📈 ML Model Benchmarks",
            "📁 Dataset & Methodology"
        ],
        index=0
    )
    
    st.markdown("---")
    st.markdown("**📌 Key Project Facts:**")
    st.caption("• **Data Source**: Ministry of Agriculture & IMD")
    st.caption("• **Dataset Scope**: 19,689 Records | 55 Crops | 30 States")
    st.caption("• **Champion Model**: Random Forest (96.75% Test R²)")
    st.caption("• **Evaluation Integrity**: Zero Target Leakage")


# =========================================================
# 1. PROJECT OVERVIEW & EXECUTIVE SUMMARY
# =========================================================
if section == "🎯 Project Overview":
    st.markdown("""
    <div class="hero-banner">
        <h1>AgriYield: AI-Based Crop Yield Forecasting</h1>
        <p>An end-to-end data science investigation analyzing 24 years of agricultural census records across India to model and predict crop yield prior to harvest.</p>
        <div class="badge-container">
            <span class="badge-pill">📊 19,689 Real Census Records</span>
            <span class="badge-pill">⭐ 96.75% Test R² Accuracy</span>
            <span class="badge-pill">🛡️ Strict Leakage-Free Pipeline</span>
            <span class="badge-pill">🤖 4 Models Benchmarked</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # 4 Key Metric Cards
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-label">Dataset Records</div>
            <div class="metric-val">{len(df):,}</div>
            <div class="metric-sub">1997–2020 longitudinal census</div>
        </div>
        """, unsafe_allow_html=True)
    with m2:
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-label">Crops & States</div>
            <div class="metric-val">{df['Crop'].nunique()} <span style="font-size:1.1rem; color:#94a3b8;">crops / </span>{df['State'].nunique()} <span style="font-size:1.1rem; color:#94a3b8;">states</span></div>
            <div class="metric-sub">Nationwide coverage</div>
        </div>
        """, unsafe_allow_html=True)
    with m3:
        best_r2 = comp_data.get('comparison', [{}])[2].get('test_r2', 0.9675)
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-label">Predictive Accuracy</div>
            <div class="metric-val">{best_r2 * 100:.1f}% <span style="font-size:1rem; color:#10b981;">R²</span></div>
            <div class="metric-sub">Unseen test holdout (2016–2020)</div>
        </div>
        """, unsafe_allow_html=True)
    with m4:
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-label">Target Data Leakage</div>
            <div class="metric-val" style="color:#38bdf8;">0.00%</div>
            <div class="metric-sub">Post-harvest production omitted</div>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("<div style='height:15px;'></div>", unsafe_allow_html=True)
    
    c_left, c_right = st.columns(2)
    with c_left:
        st.markdown("""
        <div class="card">
            <h3>❓ The Core Research Problem</h3>
            <p>Traditional agricultural yield estimation relies on manual crop-cutting experiments conducted <i>after</i> harvest, 
            which are labor-intensive, logistically delayed, and incapable of providing early warning for food supply planning.</p>
            <p><b>Research Objective:</b> Can we predict crop yield <b>months before harvest</b> using pre-sowing and growing season factors (weather, chemical inputs, geography, and crop species)?</p>
            <ul>
                <li><b>Input Predictors:</b> Crop type, State, Season, Cultivated Area, Annual Rainfall, Fertilizer, Pesticide.</li>
                <li><b>Target Variable:</b> Crop Yield (Tonnes/Ha).</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with c_right:
        st.markdown("""
        <div class="card">
            <h3>💡 Key Scientific Discoveries</h3>
            <ol>
                <li><b>Crop Genetics Form the Yield Ceiling:</b> The crop species alone accounts for <b>~72%</b> of predictive importance. Sugarcane (~50 t/ha) and Potato (~13 t/ha) naturally produce vastly higher physical tonnage than cereal grains (2–4 t/ha) or pulses (0.5–1.0 t/ha).</li>
                <li><b>Simpson's Paradox in Fertilizer:</b> Chemical fertilizers correlate positively with yield for heavy cash crops (+0.17 for Sugarcane), but show near-zero or negative correlation in pulses because legumes fix their own nitrogen.</li>
                <li><b>Diminishing Rainfall Returns:</b> Rainfall improves yield up to ~2,000 mm, but excessive rainfall beyond that causes waterlogging and fungal risks, capping productivity.</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)


# =========================================================
# 2. LIVE PREDICTION SIMULATOR
# =========================================================
elif section == "🔮 Live Prediction Simulator":
    st.markdown("## 🔮 Pre-Harvest Yield Prediction Simulator")
    st.markdown("Simulate pre-harvest agronomic scenarios to compute real-time yield forecasts, total expected biomass, and regional benchmarks.")
    
    # Quick Demonstration Scenarios
    st.markdown("<p class='preset-title'>⚡ Quick Demonstration Scenarios:</p>", unsafe_allow_html=True)
    p_col1, p_col2, p_col3 = st.columns(3)
    
    # Initialize session state
    if "p_crop" not in st.session_state:
        st.session_state.p_crop = "Wheat"
        st.session_state.p_state = "Punjab"
        st.session_state.p_season = "Rabi"
        st.session_state.p_area = 10000.0
        st.session_state.p_rain = 650.0
        st.session_state.p_fert = 1400000.0
        st.session_state.p_pest = 4000.0
        st.session_state.calculated = False
        
    if p_col1.button("🌾 Scenario A: Punjab Wheat (Rabi Season)", use_container_width=True):
        st.session_state.p_crop = "Wheat"
        st.session_state.p_state = "Punjab"
        st.session_state.p_season = "Rabi"
        st.session_state.p_area = 10000.0
        st.session_state.p_rain = 650.0
        st.session_state.p_fert = 1400000.0
        st.session_state.p_pest = 4000.0
        st.session_state.calculated = True
        st.rerun()
        
    if p_col2.button("🍚 Scenario B: West Bengal Rice (Kharif Season)", use_container_width=True):
        st.session_state.p_crop = "Rice"
        st.session_state.p_state = "West Bengal"
        st.session_state.p_season = "Kharif"
        st.session_state.p_area = 15000.0
        st.session_state.p_rain = 1750.0
        st.session_state.p_fert = 1800000.0
        st.session_state.p_pest = 4500.0
        st.session_state.calculated = True
        st.rerun()
        
    if p_col3.button("🎋 Scenario C: Maharashtra Sugarcane (Commercial Cash Crop)", use_container_width=True):
        st.session_state.p_crop = "Sugarcane"
        st.session_state.p_state = "Maharashtra"
        st.session_state.p_season = "Whole Year"
        st.session_state.p_area = 20000.0
        st.session_state.p_rain = 1150.0
        st.session_state.p_fert = 2800000.0
        st.session_state.p_pest = 6000.0
        st.session_state.calculated = True
        st.rerun()

    st.markdown("<div style='height:8px;'></div>", unsafe_allow_html=True)
    
    with st.container(border=True):
        col1, col2, col3 = st.columns(3)
        with col1:
            all_crops = sorted(df['Crop'].unique().tolist())
            idx_c = all_crops.index(st.session_state.p_crop) if st.session_state.p_crop in all_crops else 0
            in_crop = st.selectbox("Crop Species:", all_crops, index=idx_c)
            
            all_states = sorted(df['State'].unique().tolist())
            idx_s = all_states.index(st.session_state.p_state) if st.session_state.p_state in all_states else 0
            in_state = st.selectbox("Cultivation State:", all_states, index=idx_s)
            
        with col2:
            all_seasons = sorted(df['Season'].unique().tolist())
            idx_sea = all_seasons.index(st.session_state.p_season) if st.session_state.p_season in all_seasons else 0
            in_season = st.selectbox("Cropping Season:", all_seasons, index=idx_sea)
            
            in_year = st.slider("Harvest Year:", 1997, 2026, 2024)
            
        with col3:
            in_area = st.number_input("Cultivated Area (Hectares):", min_value=1.0, max_value=500000.0, value=float(st.session_state.p_area), step=500.0,
                                      help="District or regional cultivated acreage.")
            in_rain = st.number_input("Annual Precipitation (mm):", min_value=100.0, max_value=6500.0, value=float(st.session_state.p_rain), step=50.0)
            
        col4, col5 = st.columns(2)
        with col4:
            in_fert = st.number_input("Total Fertilizer Applied (kg):", min_value=0.0, max_value=50000000.0, value=float(st.session_state.p_fert), step=50000.0)
        with col5:
            in_pest = st.number_input("Total Pesticide Applied (kg):", min_value=0.0, max_value=1000000.0, value=float(st.session_state.p_pest), step=500.0)
            
        fert_rate = in_fert / in_area if in_area > 0 else 0
        pest_rate = in_pest / in_area if in_area > 0 else 0
        st.caption(f"⚡ Agronomic Intensities: **{fert_rate:.1f} kg/ha** fertilizer rate | **{pest_rate:.2f} kg/ha** pesticide rate")
        
        calc_btn = st.button("🚀 Calculate Predicted Yield", type="primary", use_container_width=True)
        
    if calc_btn:
        st.session_state.calculated = True

    # ---------------------------------------------------------
    # Dynamic, Understandable Output Presentation Area
    # ---------------------------------------------------------
    if st.session_state.get("calculated", False):
        with st.spinner("Processing agronomic inputs through Random Forest pipeline..."):
            pred_out = predict_crop_yield(
                crop=in_crop,
                state=in_state,
                season=in_season,
                crop_year=in_year,
                area=in_area,
                annual_rainfall=in_rain,
                fertilizer=in_fert,
                pesticide=in_pest
            )
            
        # Calculate historical benchmarks from actual dataset
        crop_sub = df[df['Crop'] == in_crop]
        nat_avg = float(crop_sub['Yield'].mean()) if len(crop_sub) > 0 else 0.0
        
        state_crop_sub = df[(df['Crop'] == in_crop) & (df['State'] == in_state)]
        state_avg = float(state_crop_sub['Yield'].mean()) if len(state_crop_sub) > 0 else nat_avg
        
        pred_val = pred_out['predicted_yield']
        tot_tonnes = pred_val * in_area
        
        # Determine performance badge
        if pred_val >= 1.05 * state_avg:
            tier_badge = "🟢 Favorable Yield Tier (Above State Average)"
            tier_color = "#10b981"
        elif pred_val <= 0.85 * state_avg:
            tier_badge = "🟠 Sub-Optimal Yield Tier (Below State Average)"
            tier_color = "#f59e0b"
        else:
            tier_badge = "🔵 Standard Expected Productivity Tier"
            tier_color = "#0284c7"
            
        st.markdown("---")
        
        # 1. Plain-Language Harvest Forecast Summary
        acre_equiv = in_area * 2.471
        yield_per_acre = pred_val / 2.471
        
        st.markdown(f"""
        <div class="summary-box">
            <h3>🌾 Simple Harvest Forecast Summary</h3>
            <p>
                For your <b>{in_area:,.0f} hectares</b> (approx. <b>{acre_equiv:,.0f} acres</b>) of <b>{in_crop}</b> in <b>{in_state}</b>:
                <br>• Expected harvest rate: <b>{pred_val:.2f} tonnes per hectare</b> (about <b>{yield_per_acre:.2f} tonnes per acre</b>).
                <br>• Total crop you will harvest: approximately <b>{tot_tonnes:,.0f} metric tonnes</b>.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # 2. Three Clear Everyday Metric Cards
        res1, res2, res3 = st.columns(3)
        with res1:
            st.markdown(f"""
            <div class="metric-box" style="border-top-color:{tier_color};">
                <div class="metric-label">🌾 Harvest Rate Per Hectare</div>
                <div class="metric-val">{pred_val:.2f} <span style="font-size:1.1rem; color:#94a3b8;">t/ha</span></div>
                <div class="metric-sub">
                    <b>≈ {yield_per_acre:.2f} tonnes per acre</b><br>
                    <span style="color:{tier_color}; font-weight:600;">{tier_badge}</span><br>
                    What 1 hectare (2.5 acres) will produce
                </div>
            </div>
            """, unsafe_allow_html=True)
        with res2:
            st.markdown(f"""
            <div class="metric-box" style="border-top-color:#38bdf8;">
                <div class="metric-label">🚜 Total Harvest (All Land)</div>
                <div class="metric-val" style="font-size:1.7rem; color:#38bdf8;">
                    {tot_tonnes:,.0f} <span style="font-size:1.1rem; color:#94a3b8;">tonnes</span>
                </div>
                <div class="metric-sub">
                    From all <b>{in_area:,.0f} hectares</b> combined<br>
                    ≈ <b>{max(1, int(tot_tonnes/10)):,}</b> standard 10-tonne truckloads<br>
                    Total weight to take to market or mill
                </div>
            </div>
            """, unsafe_allow_html=True)
        with res3:
            st.markdown(f"""
            <div class="metric-box" style="border-top-color:#a855f7;">
                <div class="metric-label">🌦️ Expected Weather Range</div>
                <div class="metric-val" style="font-size:1.55rem; color:#c084fc;">
                    {pred_out['lower_bound']:.1f} – {pred_out['upper_bound']:.1f} <span style="font-size:1rem; color:#94a3b8;">t/ha</span>
                </div>
                <div class="metric-sub">
                    Dry/Poor Season: <b>{pred_out['lower_bound']:.1f} t/ha</b><br>
                    Favorable/Good Season: <b>{pred_out['upper_bound']:.1f} t/ha</b><br>
                    Accounts for normal monsoon fluctuations
                </div>
            </div>
            """, unsafe_allow_html=True)
            
        st.markdown("<div style='height:15px;'></div>", unsafe_allow_html=True)
        
        # 3. Simple Visual Benchmark Chart
        st.subheader("📊 How Does Your Prediction Compare to Real Averages?")
        st.caption("Comparison against actual historical government census records:")
        
        bench_df = pd.DataFrame([
            {"Label": "Your Farm Forecast", "Yield (t/ha)": round(pred_val, 2), "Color": "#10b981"},
            {"Label": f"Typical Farm in {in_state}", "Yield (t/ha)": round(state_avg, 2), "Color": "#38bdf8"},
            {"Label": f"All-India Average for {in_crop}", "Yield (t/ha)": round(nat_avg, 2), "Color": "#94a3b8"}
        ])
        
        fig_bench = go.Figure()
        fig_bench.add_trace(go.Bar(
            y=bench_df['Label'],
            x=bench_df['Yield (t/ha)'],
            orientation='h',
            marker_color=bench_df['Color'],
            text=[f"<b>{v:.2f} tonnes/ha</b>  ({v/2.471:.2f} t/acre)" for v in bench_df['Yield (t/ha)']],
            textposition='outside'
        ))
        bench_layout = dict(THEME_LAYOUT)
        bench_layout.update(
            height=260,
            xaxis_title="Yield in Metric Tonnes per Hectare",
            yaxis=dict(autorange="reversed"),
            margin=dict(l=20, r=40, t=20, b=30)
        )
        fig_bench.update_layout(bench_layout)
        st.plotly_chart(fig_bench, use_container_width=True)
        
        # 4. Simple Explanation of Conditions
        st.markdown(f"""
        <div class="insight-card">
            <b>💡 Summary of Conditions Evaluated:</b><br>
            • <b>Annual Rainfall:</b> {in_rain:,.0f} mm per year (water supply)<br>
            • <b>Fertilizer Application:</b> {fert_rate:.1f} kg per hectare<br>
            • <b>Pesticide Application:</b> {pest_rate:.2f} kg per hectare<br>
            • <b>Regional Comparison:</b> Your predicted harvest of <b>{pred_val:.2f} t/ha</b> is 
            {'higher than' if pred_val >= state_avg else 'slightly lower than' if pred_val < 0.95*state_avg else 'very close to'} 
            the historical average of <b>{state_avg:.2f} t/ha</b> recorded in {in_state}.
        </div>
        """, unsafe_allow_html=True)
    else:
        st.info("👉 Select your agricultural parameters above and click **'Calculate Predicted Yield'**, or select one of the **Quick Demonstration Scenarios** to run the prediction model.")


# =========================================================
# 3. CORE AGRICULTURAL INSIGHTS
# =========================================================
elif section == "📊 Core Agricultural Insights":
    st.markdown("## 📊 Core Agricultural Insights")
    st.markdown("Key empirical findings and interactive charts demonstrating how crop yield varies across species, regions, and climate.")
    
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("1. Yield Hierarchy by Crop Species")
        field_df = df[df['Crop'] != 'Coconut']
        top_crops = field_df.groupby('Crop')['Yield'].mean().sort_values(ascending=False).head(10).reset_index()
        fig_crop = px.bar(
            top_crops,
            x='Yield',
            y='Crop',
            orientation='h',
            color='Yield',
            color_continuous_scale="Tealgrn",
            labels={'Yield': 'Mean Yield (Tonnes/Ha)', 'Crop': ''}
        )
        fig_crop.update_layout(**THEME_LAYOUT, height=360, yaxis=dict(autorange="reversed"))
        st.plotly_chart(fig_crop, use_container_width=True)
        st.markdown("""
        <div class="insight-card">
            <b>💡 Agronomic Finding:</b> Sugarcane (~52 t/ha), Banana (~27 t/ha), and Potato (~13 t/ha) dominate biomass production. 
            Cereal grains (Rice, Wheat, Maize) yield 2–4 t/ha, while protein-dense pulses yield ~0.5–1 t/ha due to higher metabolic energy requirements.
        </div>
        """, unsafe_allow_html=True)
        
    with c2:
        st.subheader("2. Regional Productivity Leaderboard")
        top_states = field_df.groupby('State')['Yield'].mean().sort_values(ascending=False).head(10).reset_index()
        fig_state = px.bar(
            top_states,
            x='State',
            y='Yield',
            color='Yield',
            color_continuous_scale="Mint",
            labels={'Yield': 'Avg Yield (t/ha)', 'State': ''}
        )
        fig_state.update_layout(**THEME_LAYOUT, height=360, xaxis_tickangle=-35)
        st.plotly_chart(fig_state, use_container_width=True)
        st.markdown("""
        <div class="insight-card">
            <b>💡 Regional Finding:</b> States with widespread canal irrigation and fertile soils (Punjab 4.2 t/ha, Tamil Nadu 3.9 t/ha) 
            significantly outpace rainfed plateau regions (Rajasthan 1.2 t/ha).
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("---")
    
    c3, c4 = st.columns(2)
    with c3:
        st.subheader("3. Historical Drought Sensitivity (1997–2020)")
        major_crops = ['Rice', 'Wheat', 'Maize', 'Sugarcane']
        sub_time = field_df[field_df['Crop'].isin(major_crops)].groupby(['Crop_Year', 'Crop'])['Yield'].mean().reset_index()
        fig_time = px.line(
            sub_time,
            x='Crop_Year',
            y='Yield',
            color='Crop',
            markers=True,
            labels={'Crop_Year': 'Year', 'Yield': 'Yield (t/ha)'}
        )
        fig_time.update_layout(**THEME_LAYOUT, height=360)
        st.plotly_chart(fig_time, use_container_width=True)
        st.markdown("""
        <div class="insight-card">
            <b>💡 Climate Sensitivity:</b> Notice the sharp productivity dips in <b>2002</b>, <b>2009</b>, and <b>2014–2015</b>. 
            These empirically mirror major nationwide El Niño monsoon droughts recorded by the Meteorological Department.
        </div>
        """, unsafe_allow_html=True)
        
    with c4:
        st.subheader("4. Simpson's Paradox: Fertilizer Response")
        sample_scat = field_df[field_df['Crop'].isin(['Sugarcane', 'Potato', 'Wheat', 'Moong(Green Gram)'])].sample(1200, random_state=42)
        sample_scat['Fertilizer_per_Area'] = sample_scat['Fertilizer'] / sample_scat['Area']
        fig_scat = px.scatter(
            sample_scat,
            x='Fertilizer_per_Area',
            y='Yield',
            color='Crop',
            opacity=0.6,
            labels={'Fertilizer_per_Area': 'Fertilizer (kg/ha)', 'Yield': 'Yield (t/ha)'}
        )
        fig_scat.update_xaxes(type="log")
        fig_scat.update_yaxes(type="log")
        fig_scat.update_layout(**THEME_LAYOUT, height=360)
        st.plotly_chart(fig_scat, use_container_width=True)
        st.markdown("""
        <div class="insight-card">
            <b>💡 Simpson's Paradox:</b> In cash crops (Sugarcane/Potato), fertilizer correlates positively (+0.17), 
            whereas in pulses (Moong), it has an inverse correlation because legumes fix their own nitrogen and excess fertilizer harms pod yield.
        </div>
        """, unsafe_allow_html=True)


# =========================================================
# 4. ML MODEL BENCHMARKS & EVALUATION
# =========================================================
elif section == "📈 ML Model Benchmarks":
    st.markdown("## 📈 Machine Learning Benchmarks & Model Selection")
    st.markdown("We trained and compared 4 regression algorithms using a strict **Time-Aware Temporal Split** (Train on 1997–2015, Test on 2016–2020 holdout).")
    
    comp_list = comp_data.get("comparison", [])
    if comp_list:
        comp_df = pd.DataFrame(comp_list)
        
        # Display clean leaderboard
        st.subheader("🏆 Model Leaderboard Matrix")
        st.dataframe(
            comp_df[['model_name', 'train_r2', 'cv_r2_mean', 'test_r2', 'test_rmse', 'test_mae']].rename(columns={
                'model_name': 'Model Architecture',
                'train_r2': 'Train R²',
                'cv_r2_mean': '5-Fold CV R²',
                'test_r2': 'Holdout Test R²',
                'test_rmse': 'Test RMSE (t/ha)',
                'test_mae': 'Test MAE (t/ha)'
            }),
            use_container_width=True,
            hide_index=True
        )
        
        st.markdown("""
        <div class="insight-card">
            <b>🏆 Model Selection Analysis:</b> <b>Random Forest Regressor</b> achieved the highest test explanatory power 
            (<b>Test R² = 96.75%</b>) and lowest error (<b>MAE = 10.95 t/ha</b>, <b>RMSE = 153.50 t/ha</b>). 
            Linear Regression underfits (59.6% R²) because real agricultural yields follow non-linear biological thresholds.
        </div>
        """, unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        with c1:
            st.subheader("Train vs. Cross-Validation vs. Test R²")
            fig_bar = go.Figure()
            fig_bar.add_trace(go.Bar(x=comp_df['model_name'], y=comp_df['train_r2'], name="Train R²", marker_color="#94a3b8"))
            fig_bar.add_trace(go.Bar(x=comp_df['model_name'], y=comp_df['cv_r2_mean'], name="5-Fold CV R²", marker_color="#f59e0b"))
            fig_bar.add_trace(go.Bar(x=comp_df['model_name'], y=comp_df['test_r2'], name="Holdout Test R²", marker_color="#10b981"))
            fig_bar.update_layout(**THEME_LAYOUT, barmode='group', height=380, yaxis=dict(range=[0, 1.05]), xaxis_title="")
            st.plotly_chart(fig_bar, use_container_width=True)
            
        with c2:
            st.subheader("Actual vs. Predicted Yield (Holdout 2016–2020)")
            sub_eval = test_preds.sample(1200, random_state=42)
            fig_eval = px.scatter(
                sub_eval,
                x='Actual_Yield',
                y='Pred_Random Forest',
                color='Crop',
                opacity=0.6,
                labels={'Actual_Yield': 'Actual Yield (t/ha)', 'Pred_Random Forest': 'Predicted Yield (t/ha)'}
            )
            fig_eval.add_trace(go.Scatter(
                x=[0.1, 1000], y=[0.1, 1000],
                mode='lines', line=dict(color='#ef4444', dash='dash', width=2),
                name='Ideal (y = x)'
            ))
            fig_eval.update_xaxes(type="log")
            fig_eval.update_yaxes(type="log")
            fig_eval.update_layout(**THEME_LAYOUT, height=380)
            st.plotly_chart(fig_eval, use_container_width=True)
            
    st.markdown("---")
    st.subheader("🧬 Feature Importance: What Drives Crop Yield?")
    
    feat_imp_path = os.path.join(os.path.dirname(__file__), "models", "feature_importance.json")
    if os.path.exists(feat_imp_path):
        with open(feat_imp_path) as f:
            f_data = json.load(f)
        grouped = f_data["Random Forest"]["grouped_feature_importance_pct"]
        gdf = pd.DataFrame([{"Feature": k, "Importance (%)": v} for k, v in grouped.items()]).sort_values("Importance (%)", ascending=True)
        
        fig_feat = px.bar(
            gdf,
            x="Importance (%)",
            y="Feature",
            orientation="h",
            color="Importance (%)",
            color_continuous_scale="Tealgrn"
        )
        fig_feat.update_layout(**THEME_LAYOUT, height=360)
        st.plotly_chart(fig_feat, use_container_width=True)
        
        st.markdown("""
        <div class="insight-card">
            <b>🔍 Feature Attribution:</b> 
            <b>Crop Species (71.8%)</b> is the primary driver, followed by <b>State Geography (11.4%)</b> (soil and canal access), 
            <b>Fertilizer Application Intensity (6.1%)</b>, and <b>Annual Rainfall (3.8%)</b>.
        </div>
        """, unsafe_allow_html=True)


# =========================================================
# 5. DATASET & METHODOLOGY
# =========================================================
elif section == "📁 Dataset & Methodology":
    st.markdown("## 📁 Dataset Provenance & Methodology")
    st.markdown("Authentic data engineering pipeline and dataset inspection.")
    
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("""
        - **Source:** Directorate of Economics and Statistics (DES), Ministry of Agriculture and Farmers Welfare, Govt. of India.
        - **Precipitation:** India Meteorological Department (IMD) historical records.
        - **Data Integrity:** 19,689 records with **100% completeness** (0 missing cells, 0 duplicate rows).
        """)
    with col2:
        csv_bytes = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            "📥 Download Cleaned CSV",
            data=csv_bytes,
            file_name="agriyield_cleaned_dataset.csv",
            mime="text/csv",
            use_container_width=True
        )
        
    st.markdown("### 🔬 4-Step Academic Workflow")
    st.markdown("""
    <div class="card">
        <ol style="margin-bottom:0; line-height:1.7;">
            <li><b>Data Audit & Cleaning:</b> Ingested 19,689 records, stripped string whitespaces, isolated Coconut scale discrepancy, and verified physical non-negativity.</li>
            <li><b>Data Leakage Prevention:</b> Strictly dropped <i>Production</i> because Yield = Production / Area. Only pre-harvest conditions are used as features.</li>
            <li><b>Temporal Train/Test Split:</b> Trained on historical years (1997–2015, 15,404 rows) with 5-fold CV; tested on future holdout years (2016–2020, 4,285 rows).</li>
            <li><b>Ensemble Modeling & Inference:</b> Fitted Random Forest under target log-transform ($f(y)=\\ln(1+y)$) to guarantee positive yield predictions and high accuracy.</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("📄 Interactive Data Sample (First 20 Records)")
    st.dataframe(df.head(20), use_container_width=True)
    
    st.subheader("📊 Descriptive Statistics")
    st.dataframe(df.describe().T, use_container_width=True)
