"""
AgriYield - PowerPoint Presentation Generator (6 Slides)
Creates a modern, executive 16:9 widescreen presentation with:
- S. SANDHIYA (ROLL NO : 24VNM034) on the front slide
- Professional emerald & dark slate agricultural design
- Neat, short, high-impact bullet points
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

PPTX_PATH = os.path.join(os.path.dirname(__file__), "AgriYield_Presentation.pptx")

# Palette
DARK_BG = RGBColor(14, 19, 31)         # #0e131f
CARD_BG = RGBColor(24, 34, 52)         # #182234
EMERALD = RGBColor(16, 185, 129)       # #10b981
FOREST_DEEP = RGBColor(6, 78, 59)      # #064e3b
LIGHT_TEXT = RGBColor(241, 245, 249)   # #f1f5f9
MUTED_TEXT = RGBColor(148, 163, 184)   # #94a3b8
ACCENT_BLUE = RGBColor(56, 189, 248)   # #38bdf8
WHITE = RGBColor(255, 255, 255)


def add_header(slide, title_text, category_text="AGRIYIELD — DATA SCIENCE PROJECT"):
    """Adds a standard stylish header to content slides."""
    # Top banner pill / category
    cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.4))
    tf_c = cat_box.text_frame
    tf_c.word_wrap = True
    p_c = tf_c.paragraphs[0]
    p_c.text = category_text.upper()
    p_c.font.size = Pt(10)
    p_c.font.bold = True
    p_c.font.color.rgb = EMERALD
    
    # Title
    title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.7), Inches(11.7), Inches(0.7))
    tf_t = title_box.text_frame
    tf_t.word_wrap = True
    p_t = tf_t.paragraphs[0]
    p_t.text = title_text
    p_t.font.size = Pt(24)
    p_t.font.bold = True
    p_t.font.color.rgb = LIGHT_TEXT


def set_slide_background(slide, color=DARK_BG):
    """Sets background fill of a slide."""
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = color


def create_presentation():
    prs = Presentation()
    # 16:9 widescreen
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # ========================================================
    # SLIDE 1: COVER SLIDE
    # ========================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1, DARK_BG)

    # Accent decorative banner top
    banner = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(0.8), Inches(11.733), Inches(0.12))
    banner.fill.solid()
    banner.fill.fore_color.rgb = EMERALD
    banner.line.color.rgb = EMERALD

    # Project Tag
    tag_box = s1.shapes.add_textbox(Inches(0.8), Inches(1.2), Inches(11.733), Inches(0.4))
    p_tag = tag_box.text_frame.paragraphs[0]
    p_tag.text = "ACADEMIC DATA SCIENCE PROJECT  •  MACHINE LEARNING & ANALYTICS"
    p_tag.font.size = Pt(11)
    p_tag.font.bold = True
    p_tag.font.color.rgb = EMERALD

    # Main Title
    t_box = s1.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(11.733), Inches(1.5))
    tf = t_box.text_frame
    tf.word_wrap = True
    p_title = tf.paragraphs[0]
    p_title.text = "AgriYield: Data Science-Based Crop Yield\nAnalysis and Prediction"
    p_title.font.size = Pt(32)
    p_title.font.bold = True
    p_title.font.color.rgb = WHITE

    # Subtitle
    sub_box = s1.shapes.add_textbox(Inches(0.8), Inches(3.3), Inches(11.733), Inches(0.6))
    p_sub = sub_box.text_frame.paragraphs[0]
    p_sub.text = "AI-Driven Pre-Harvest Yield Forecasting Using 24 Years of Indian Agricultural Census Data"
    p_sub.font.size = Pt(15)
    p_sub.font.color.rgb = MUTED_TEXT

    # Presenter Card (Highlighted)
    card_shape = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(4.3), Inches(5.8), Inches(2.3))
    card_shape.fill.solid()
    card_shape.fill.fore_color.rgb = CARD_BG
    card_shape.line.color.rgb = EMERALD
    card_shape.line.width = Pt(2)

    c_box = s1.shapes.add_textbox(Inches(1.1), Inches(4.5), Inches(5.2), Inches(1.9))
    c_tf = c_box.text_frame
    c_tf.word_wrap = True
    
    p_pres = c_tf.paragraphs[0]
    p_pres.text = "PRESENTED BY:"
    p_pres.font.size = Pt(10)
    p_pres.font.bold = True
    p_pres.font.color.rgb = EMERALD
    
    p_name = c_tf.add_paragraph()
    p_name.text = "S. SANDHIYA"
    p_name.font.size = Pt(22)
    p_name.font.bold = True
    p_name.font.color.rgb = WHITE
    p_name.space_before = Pt(4)

    p_roll = c_tf.add_paragraph()
    p_roll.text = "ROLL NO : 24VNM034"
    p_roll.font.size = Pt(14)
    p_roll.font.bold = True
    p_roll.font.color.rgb = ACCENT_BLUE
    p_roll.space_before = Pt(4)

    # Project Metric Highlights on Right
    m_shape = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.9), Inches(4.3), Inches(5.6), Inches(2.3))
    m_shape.fill.solid()
    m_shape.fill.fore_color.rgb = CARD_BG
    m_shape.line.color.rgb = RGBColor(51, 65, 85)

    m_box = s1.shapes.add_textbox(Inches(7.2), Inches(4.5), Inches(5.0), Inches(1.9))
    m_tf = m_box.text_frame
    m_tf.word_wrap = True
    
    p_k = m_tf.paragraphs[0]
    p_k.text = "KEY PROJECT HIGHLIGHTS:"
    p_k.font.size = Pt(10)
    p_k.font.bold = True
    p_k.font.color.rgb = EMERALD
    
    bullets = [
        "19,689 Real Census Records (1997–2020 longitudinal series)",
        "55 Crops & 30 Indian States Nationwide Coverage",
        "Champion Model: Random Forest Regressor (96.8% Test R²)",
        "Zero Target Data Leakage (Strict Pre-Harvest Predictors)"
    ]
    for b in bullets:
        p_b = m_tf.add_paragraph()
        p_b.text = f"•  {b}"
        p_b.font.size = Pt(11)
        p_b.font.color.rgb = LIGHT_TEXT
        p_b.space_before = Pt(3)


    # ========================================================
    # SLIDE 2: RESEARCH PROBLEM & OBJECTIVE
    # ========================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_background(s2, DARK_BG)
    add_header(s2, "1. Research Motivation & Core Objectives")

    # Left Column: The Real-World Problem
    c1 = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.7), Inches(5.6), Inches(5.0))
    c1.fill.solid()
    c1.fill.fore_color.rgb = CARD_BG
    c1.line.color.rgb = RGBColor(239, 68, 68)  # Red accent
    c1.line.width = Pt(1.5)

    tb1 = s2.shapes.add_textbox(Inches(1.1), Inches(1.9), Inches(5.0), Inches(4.5))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    
    p1 = tf1.paragraphs[0]
    p1.text = "⚠️ THE TRADITIONAL PROBLEM"
    p1.font.size = Pt(14)
    p1.font.bold = True
    p1.font.color.rgb = RGBColor(239, 68, 68)

    pts1 = [
        ("Post-Harvest Delay: ", "Yield is historically measured only after harvesting through manual Crop Cutting Experiments (CCEs)."),
        ("Logistical Strain: ", "By the time data is collected, critical food supply shortages and price inflation have already occurred."),
        ("No Early Warning: ", "Policymakers and farmers lack advance warning to plan cold-storage, transport, or MSP procurement.")
    ]
    for title, desc in pts1:
        p = tf1.add_paragraph()
        p.text = f"• {title}{desc}"
        p.font.size = Pt(12)
        p.font.color.rgb = LIGHT_TEXT
        p.space_before = Pt(12)

    # Right Column: The AgriYield Solution
    c2 = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.9), Inches(1.7), Inches(5.6), Inches(5.0))
    c2.fill.solid()
    c2.fill.fore_color.rgb = CARD_BG
    c2.line.color.rgb = EMERALD
    c2.line.width = Pt(1.5)

    tb2 = s2.shapes.add_textbox(Inches(7.2), Inches(1.9), Inches(5.0), Inches(4.5))
    tf2 = tb2.text_frame
    tf2.word_wrap = True
    
    p2 = tf2.paragraphs[0]
    p2.text = "💡 THE AGRIYIELD SOLUTION"
    p2.font.size = Pt(14)
    p2.font.bold = True
    p2.font.color.rgb = EMERALD

    pts2 = [
        ("Pre-Harvest Prediction: ", "Predict crop yield months before harvest using environmental and input factors available during sowing."),
        ("Multi-Factor Intelligence: ", "Analyzes rainfall, fertilizer rate, pesticide rate, land area, geography, and crop species simultaneously."),
        ("Practical Decision Making: ", "Translates mathematical yield (t/ha) into acre yields and commercial truckload counts for everyday logistics.")
    ]
    for title, desc in pts2:
        p = tf2.add_paragraph()
        p.text = f"• {title}{desc}"
        p.font.size = Pt(12)
        p.font.color.rgb = LIGHT_TEXT
        p.space_before = Pt(12)


    # ========================================================
    # SLIDE 3: DATASET & DATA LEAKAGE DEFENSE
    # ========================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_background(s3, DARK_BG)
    add_header(s3, "2. Dataset Scope & Data Leakage Prevention")

    # 3 Stat Cards across top
    stats = [
        ("19,689", "CENSUS RECORDS", "1997–2020 Longitudinal Series", EMERALD),
        ("55 Crops / 30 States", "GEOGRAPHIC DIVERSITY", "All Major Indian Agro-Zones", ACCENT_BLUE),
        ("0.00%", "TARGET LEAKAGE", "Production Strictly Omitted", RGBColor(168, 85, 247))
    ]
    for idx, (val, title, sub, color) in enumerate(stats):
        x = Inches(0.8 + idx * 4.0)
        c = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.6), Inches(3.7), Inches(1.5))
        c.fill.solid()
        c.fill.fore_color.rgb = CARD_BG
        c.line.color.rgb = color
        c.line.width = Pt(1.5)

        tb = s3.shapes.add_textbox(x + Inches(0.2), Inches(1.7), Inches(3.3), Inches(1.3))
        tf = tb.text_frame
        
        p_t = tf.paragraphs[0]
        p_t.text = title
        p_t.font.size = Pt(9)
        p_t.font.bold = True
        p_t.font.color.rgb = MUTED_TEXT

        p_v = tf.add_paragraph()
        p_v.text = val
        p_v.font.size = Pt(20)
        p_v.font.bold = True
        p_v.font.color.rgb = color

        p_s = tf.add_paragraph()
        p_s.text = sub
        p_s.font.size = Pt(9)
        p_s.font.color.rgb = MUTED_TEXT

    # Bottom Big Card: Leakage Defense Protocol
    c_bot = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(3.4), Inches(11.7), Inches(3.4))
    c_bot.fill.solid()
    c_bot.fill.fore_color.rgb = CARD_BG
    c_bot.line.color.rgb = EMERALD

    tb_bot = s3.shapes.add_textbox(Inches(1.1), Inches(3.6), Inches(11.1), Inches(3.0))
    tf_bot = tb_bot.text_frame
    tf_bot.word_wrap = True

    p_prot = tf_bot.paragraphs[0]
    p_prot.text = "🛡️ CRITICAL METHODOLOGY: DATA LEAKAGE DEFENSE PROTOCOL"
    p_prot.font.size = Pt(13)
    p_prot.font.bold = True
    p_prot.font.color.rgb = EMERALD

    proto_pts = [
        ("The Trivial Mathematical Trap: ", "In agricultural statistics, Yield = Total Production / Cultivated Area. Many naive projects mistakenly include 'Production' as a feature, causing models to simply divide two columns rather than predicting yield."),
        ("Our Scientific Safeguard: ", "Total Production is strictly excluded from all training and inference pipelines. Only genuine pre-harvest predictors (Crop, State, Season, Area, Rainfall, Fertilizer, Pesticide) are utilized."),
        ("Temporal Evaluation: ", "To test true future predictive capability, data was split temporally: Train on past years (1997–2015, 15,404 records) and holdout test on future years (2016–2020, 4,285 records).")
    ]
    for t, d in proto_pts:
        p = tf_bot.add_paragraph()
        p.text = f"• {t}{d}"
        p.font.size = Pt(11.5)
        p.font.color.rgb = LIGHT_TEXT
        p.space_before = Pt(8)


    # ========================================================
    # SLIDE 4: ML BENCHMARKS & MODEL SELECTION
    # ========================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_background(s4, DARK_BG)
    add_header(s4, "3. Machine Learning Models & Leaderboard Matrix")

    # Table of 4 models
    rows, cols = 5, 5
    table_shape = s4.shapes.add_table(rows, cols, Inches(0.8), Inches(1.6), Inches(11.7), Inches(2.6))
    tbl = table_shape.table

    tbl.columns[0].width = Inches(2.6)
    tbl.columns[1].width = Inches(2.2)
    tbl.columns[2].width = Inches(2.2)
    tbl.columns[3].width = Inches(2.3)
    tbl.columns[4].width = Inches(2.4)

    headers = ["Model Architecture", "Train R²", "5-Fold CV R²", "Holdout Test R²", "Test MAE (t/ha)"]
    for i, h in enumerate(headers):
        cell = tbl.cell(0, i)
        cell.text = h
        cell.fill.solid()
        cell.fill.fore_color.rgb = FOREST_DEEP
        p = cell.text_frame.paragraphs[0]
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = WHITE

    model_data = [
        ["Linear Regression (Ridge)", "58.1%", "57.8%", "59.6%", "34.12 t/ha"],
        ["Decision Tree Regressor", "99.8%", "91.2%", "92.4%", "18.45 t/ha"],
        ["Gradient Boosting Regressor", "94.8%", "93.1%", "94.1%", "15.30 t/ha"],
        ["Random Forest Regressor 🏆", "99.7%", "95.9%", "96.8%", "10.95 t/ha"]
    ]
    for r_idx, row in enumerate(model_data):
        for c_idx, val in enumerate(row):
            cell = tbl.cell(r_idx + 1, c_idx)
            cell.text = val
            cell.fill.solid()
            # Highlight champion
            if r_idx == 3:
                cell.fill.fore_color.rgb = RGBColor(16, 78, 59)
            else:
                cell.fill.fore_color.rgb = CARD_BG
            p = cell.text_frame.paragraphs[0]
            p.font.size = Pt(11)
            p.font.color.rgb = EMERALD if r_idx == 3 else LIGHT_TEXT
            if r_idx == 3:
                p.font.bold = True

    # Analysis Card Below
    c_ana = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(4.5), Inches(11.7), Inches(2.4))
    c_ana.fill.solid()
    c_ana.fill.fore_color.rgb = CARD_BG
    c_ana.line.color.rgb = EMERALD

    tb_ana = s4.shapes.add_textbox(Inches(1.1), Inches(4.6), Inches(11.1), Inches(2.1))
    tf_ana = tb_ana.text_frame
    tf_ana.word_wrap = True

    p_wh = tf_ana.paragraphs[0]
    p_wh.text = "🏆 WHY RANDOM FOREST WAS SELECTED AS THE CHAMPION MODEL:"
    p_wh.font.size = Pt(12)
    p_wh.font.bold = True
    p_wh.font.color.rgb = EMERALD

    reasons = [
        ("Non-Linear Biological Thresholds: ", "Linear Regression underfits (59.6% R²) because crop yield does not increase indefinitely with fertilizer or rain. Real crops have saturating biological thresholds."),
        ("Log-Transformation Synergy: ", "Random Forest was trained under a target log-transform (ln(1+y)), guaranteeing positive yield outputs and dramatically reducing errors on high-yield cash crops."),
        ("Generalization Power: ", "Achieved lowest test error (MAE: 10.95 t/ha) across 4,285 unseen future records from 2016 to 2020.")
    ]
    for t, d in reasons:
        p = tf_ana.add_paragraph()
        p.text = f"• {t}{d}"
        p.font.size = Pt(11)
        p.font.color.rgb = LIGHT_TEXT
        p.space_before = Pt(5)


    # ========================================================
    # SLIDE 5: KEY AGRICULTURAL FINDINGS
    # ========================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_background(s5, DARK_BG)
    add_header(s5, "4. Key Empirical Agricultural Discoveries")

    cards = [
        ("1. CROP GENETICS SET THE CEILING",
         "Feature Importance: 71.8%",
         "Crop species alone accounts for ~72% of all predictive power. Heavy cash crops (Sugarcane ~52 t/ha, Potato ~13 t/ha) naturally produce vastly higher physical tonnage than cereal grains (Wheat/Rice 2–4 t/ha) or pulses (~0.8 t/ha).",
         EMERALD),
        ("2. SIMPSON'S PARADOX IN FERTILIZER",
         "Non-Intuitive Agronomic Insight",
         "Fertilizer correlates positively (+0.17) with yield for heavy feeder crops (Sugarcane), but shows near-zero or negative correlation in pulses (Moong/Gram). Legumes biologically fix nitrogen; excess chemical fertilizer suppresses nodulation and hurts yield.",
         ACCENT_BLUE),
        ("3. DIMINISHING RAINFALL RETURNS",
         "Climate Threshold Sensitivity",
         "Precipitation strongly boosts yield up to ~2,000 mm/year. Beyond 2,000 mm, excess water triggers waterlogging, root aeration failure, and fungal spread, placing a natural ceiling on agricultural productivity.",
         RGBColor(245, 158, 11))
    ]

    for idx, (title, sub, body, color) in enumerate(cards):
        x = Inches(0.8 + idx * 4.0)
        c = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.6), Inches(3.7), Inches(5.1))
        c.fill.solid()
        c.fill.fore_color.rgb = CARD_BG
        c.line.color.rgb = color
        c.line.width = Pt(1.5)

        tb = s5.shapes.add_textbox(x + Inches(0.2), Inches(1.8), Inches(3.3), Inches(4.7))
        tf = tb.text_frame
        tf.word_wrap = True

        p_t = tf.paragraphs[0]
        p_t.text = title
        p_t.font.size = Pt(12)
        p_t.font.bold = True
        p_t.font.color.rgb = color

        p_s = tf.add_paragraph()
        p_s.text = sub
        p_s.font.size = Pt(9.5)
        p_s.font.bold = True
        p_s.font.color.rgb = MUTED_TEXT
        p_s.space_before = Pt(3)

        p_b = tf.add_paragraph()
        p_b.text = body
        p_b.font.size = Pt(11)
        p_b.font.color.rgb = LIGHT_TEXT
        p_b.space_before = Pt(12)


    # ========================================================
    # SLIDE 6: WEB APPLICATION & LIVE DEMONSTRATION
    # ========================================================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_background(s6, DARK_BG)
    add_header(s6, "5. Implementation Architecture & Live Dashboard")

    # Left: Tech Stack
    c_l = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.1))
    c_l.fill.solid()
    c_l.fill.fore_color.rgb = CARD_BG
    c_l.line.color.rgb = EMERALD

    tb_l = s6.shapes.add_textbox(Inches(1.1), Inches(1.8), Inches(5.0), Inches(4.7))
    tf_l = tb_l.text_frame
    tf_l.word_wrap = True

    p_tl = tf_l.paragraphs[0]
    p_tl.text = "💻 TECHNICAL ARCHITECTURE"
    p_tl.font.size = Pt(13)
    p_tl.font.bold = True
    p_tl.font.color.rgb = EMERALD

    techs = [
        ("Python 3.10 / 3.12: ", "Core programming language for data engineering, modeling, and dashboard."),
        ("Scikit-Learn Pipeline: ", "Encapsulates One-Hot Encoding, RobustScaler, and Random Forest for instant real-time inference."),
        ("Streamlit UI Layer: ", "Interactive web app allowing users to test farm scenarios and receive immediate predictions."),
        ("Plotly Express: ", "Dynamic interactive charts displaying comparative benchmarks and historical trends."),
        ("Streamlit Cloud: ", "Automated CI/CD deployment directly from GitHub, ensuring 24/7 global accessibility.")
    ]
    for t, d in techs:
        p = tf_l.add_paragraph()
        p.text = f"• {t}{d}"
        p.font.size = Pt(11)
        p.font.color.rgb = LIGHT_TEXT
        p.space_before = Pt(7)

    # Right: User-Facing Output
    c_r = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.9), Inches(1.6), Inches(5.6), Inches(5.1))
    c_r.fill.solid()
    c_r.fill.fore_color.rgb = CARD_BG
    c_r.line.color.rgb = ACCENT_BLUE

    tb_r = s6.shapes.add_textbox(Inches(7.2), Inches(1.8), Inches(5.0), Inches(4.7))
    tf_r = tb_r.text_frame
    tf_r.word_wrap = True

    p_tr = tf_r.paragraphs[0]
    p_tr.text = "🌾 USER-FRIENDLY DASHBOARD FEATURES"
    p_tr.font.size = Pt(13)
    p_tr.font.bold = True
    p_tr.font.color.rgb = ACCENT_BLUE

    feats = [
        ("1-Click Presets: ", "Punjab Wheat (Rabi), West Bengal Rice (Kharif), and Maharashtra Sugarcane for rapid demonstration."),
        ("Understandable Units: ", "Translates mathematical Tonnes/Hectare into Tonnes/Acre and standard 10-Tonne Truckload counts."),
        ("Benchmark Comparison: ", "Compares predicted harvest against actual state and nationwide government averages."),
        ("Dark/Light Mode: ", "100% theme-adaptive UI designed with high-contrast executive visual presentation.")
    ]
    for t, d in feats:
        p = tf_r.add_paragraph()
        p.text = f"• {t}{d}"
        p.font.size = Pt(11)
        p.font.color.rgb = LIGHT_TEXT
        p.space_before = Pt(8)

    # Save presentation
    prs.save(PPTX_PATH)
    print(f"Presentation saved successfully to: {PPTX_PATH}")


if __name__ == "__main__":
    create_presentation()
