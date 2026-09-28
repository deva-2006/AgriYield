"""
AgriYield - Short, Neat & Simple 6-Slide Presentation Generator
Designed for maximum clarity, generous whitespace, large text, and zero clutter.
Presenter: S. SANDHIYA (ROLL NO : 24VNM034)
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

PPTX_PATH = os.path.join(os.path.dirname(__file__), "AgriYield_Presentation.pptx")

DARK_BG = RGBColor(14, 19, 31)         # #0e131f
CARD_BG = RGBColor(24, 34, 52)         # #182234
EMERALD = RGBColor(16, 185, 129)       # #10b981
LIGHT_TEXT = RGBColor(241, 245, 249)   # #f1f5f9
MUTED_TEXT = RGBColor(148, 163, 184)   # #94a3b8
ACCENT_BLUE = RGBColor(56, 189, 248)   # #38bdf8
WHITE = RGBColor(255, 255, 255)


def set_bg(slide):
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = DARK_BG


def add_slide_header(slide, slide_num, title):
    # Header tag
    tag_box = slide.shapes.add_textbox(Inches(1.0), Inches(0.5), Inches(11.3), Inches(0.4))
    p_tag = tag_box.text_frame.paragraphs[0]
    p_tag.text = f"AGRIYIELD  •  SLIDE {slide_num} OF 6"
    p_tag.font.size = Pt(11)
    p_tag.font.bold = True
    p_tag.font.color.rgb = EMERALD

    # Main Title
    t_box = slide.shapes.add_textbox(Inches(1.0), Inches(0.85), Inches(11.3), Inches(0.8))
    p_title = t_box.text_frame.paragraphs[0]
    p_title.text = title
    p_title.font.size = Pt(26)
    p_title.font.bold = True
    p_title.font.color.rgb = WHITE


def create_clean_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # ========================================================
    # SLIDE 1: COVER SLIDE
    # ========================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_bg(s1)

    # Accent green line
    line = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.0), Inches(1.0), Inches(11.333), Inches(0.08))
    line.fill.solid()
    line.fill.fore_color.rgb = EMERALD
    line.line.color.rgb = EMERALD

    # Title
    t_box = s1.shapes.add_textbox(Inches(1.0), Inches(1.4), Inches(11.333), Inches(1.6))
    tf1 = t_box.text_frame
    tf1.word_wrap = True
    p1 = tf1.paragraphs[0]
    p1.text = "🌾 AgriYield: Crop Yield Prediction"
    p1.font.size = Pt(36)
    p1.font.bold = True
    p1.font.color.rgb = WHITE

    p1_sub = tf1.add_paragraph()
    p1_sub.text = "Data Science-Based Agricultural Analysis and Pre-Harvest Forecasting"
    p1_sub.font.size = Pt(16)
    p1_sub.font.color.rgb = MUTED_TEXT
    p1_sub.space_before = Pt(8)

    # Author Card (Highlighted)
    auth_card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(3.6), Inches(6.0), Inches(2.6))
    auth_card.fill.solid()
    auth_card.fill.fore_color.rgb = CARD_BG
    auth_card.line.color.rgb = EMERALD
    auth_card.line.width = Pt(2)

    at_box = s1.shapes.add_textbox(Inches(1.3), Inches(3.9), Inches(5.4), Inches(2.1))
    at_tf = at_box.text_frame
    
    p_a1 = at_tf.paragraphs[0]
    p_a1.text = "PRESENTED BY"
    p_a1.font.size = Pt(11)
    p_a1.font.bold = True
    p_a1.font.color.rgb = EMERALD

    p_a2 = at_tf.add_paragraph()
    p_a2.text = "S. SANDHIYA"
    p_a2.font.size = Pt(26)
    p_a2.font.bold = True
    p_a2.font.color.rgb = WHITE
    p_a2.space_before = Pt(6)

    p_a3 = at_tf.add_paragraph()
    p_a3.text = "ROLL NO : 24VNM034"
    p_a3.font.size = Pt(16)
    p_a3.font.bold = True
    p_a3.font.color.rgb = ACCENT_BLUE
    p_a3.space_before = Pt(6)

    # Project Scope Card
    info_card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.3), Inches(3.6), Inches(5.0), Inches(2.6))
    info_card.fill.solid()
    info_card.fill.fore_color.rgb = CARD_BG
    info_card.line.color.rgb = RGBColor(51, 65, 85)

    it_box = s1.shapes.add_textbox(Inches(7.6), Inches(3.9), Inches(4.4), Inches(2.1))
    it_tf = it_box.text_frame
    
    p_i1 = it_tf.paragraphs[0]
    p_i1.text = "PROJECT QUICK FACTS"
    p_i1.font.size = Pt(11)
    p_i1.font.bold = True
    p_i1.font.color.rgb = EMERALD

    facts = [
        "19,689 Real Census Records (1997–2020)",
        "55 Crops & 30 Indian States",
        "Champion Model: Random Forest",
        "Prediction Accuracy: 96.8% (R² Score)"
    ]
    for f in facts:
        p = it_tf.add_paragraph()
        p.text = f"✔  {f}"
        p.font.size = Pt(12)
        p.font.color.rgb = LIGHT_TEXT
        p.space_before = Pt(5)

    # ========================================================
    # SLIDE 2: THE PROBLEM & OUR OBJECTIVE
    # ========================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_bg(s2)
    add_slide_header(s2, 2, "The Real-World Problem & Our Solution")

    # Left: The Problem
    c_prob = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(1.8), Inches(5.4), Inches(4.8))
    c_prob.fill.solid()
    c_prob.fill.fore_color.rgb = CARD_BG
    c_prob.line.color.rgb = RGBColor(239, 68, 68)

    tb_p = s2.shapes.add_textbox(Inches(1.3), Inches(2.0), Inches(4.8), Inches(4.4))
    tf_p = tb_p.text_frame
    tf_p.word_wrap = True

    p = tf_p.paragraphs[0]
    p.text = "⚠️ THE PROBLEM TODAY"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = RGBColor(239, 68, 68)

    prob_items = [
        "Manual Crop-Cutting: Yield is only measured after harvest by manually cutting field samples.",
        "Too Late for Action: When food shortages occur, prices have already spiked.",
        "No Advance Planning: Farmers cannot plan storage, trucks, or sales in advance."
    ]
    for item in prob_items:
        p = tf_p.add_paragraph()
        p.text = f"•  {item}"
        p.font.size = Pt(13)
        p.font.color.rgb = LIGHT_TEXT
        p.space_before = Pt(14)

    # Right: Our Solution
    c_sol = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.9), Inches(1.8), Inches(5.4), Inches(4.8))
    c_sol.fill.solid()
    c_sol.fill.fore_color.rgb = CARD_BG
    c_sol.line.color.rgb = EMERALD

    tb_s = s2.shapes.add_textbox(Inches(7.2), Inches(2.0), Inches(4.8), Inches(4.4))
    tf_s = tb_s.text_frame
    tf_s.word_wrap = True

    p = tf_s.paragraphs[0]
    p.text = "💡 THE AGRIYIELD SOLUTION"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = EMERALD

    sol_items = [
        "Pre-Harvest Forecasting: Predicts crop yield months before harvest using planting data.",
        "Simple Everyday Inputs: Uses rainfall, fertilizer amount, land area, and crop type.",
        "Farmer-Friendly Output: Converts numbers into tonnes per acre and truckloads."
    ]
    for item in sol_items:
        p = tf_s.add_paragraph()
        p.text = f"✔  {item}"
        p.font.size = Pt(13)
        p.font.color.rgb = LIGHT_TEXT
        p.space_before = Pt(14)

    # ========================================================
    # SLIDE 3: DATASET & INTEGRITY
    # ========================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_bg(s3)
    add_slide_header(s3, 3, "The Dataset & Leakage Prevention")

    # 4 clean cards in 2x2 grid
    grid_items = [
        ("📊 19,689 Records", "24 Years of authentic Indian agricultural census records (1997 to 2020) from the Ministry of Agriculture & IMD.", EMERALD),
        ("🌾 55 Crops & 30 States", "Wide coverage across cereals (Rice, Wheat), pulses (Gram, Moong), oilseeds, and heavy cash crops (Sugarcane).", ACCENT_BLUE),
        ("🛡️ Zero Data Leakage", "Strictly excluded 'Total Production' because Yield = Production / Area. If included, the AI would cheat by dividing instead of predicting.", RGBColor(168, 85, 247)),
        ("⏳ Real Future Testing", "Trained on past years (1997–2015) and tested on unseen future years (2016–2020) to guarantee true reliability.", RGBColor(245, 158, 11))
    ]

    coords = [
        (Inches(1.0), Inches(1.8)),
        (Inches(6.9), Inches(1.8)),
        (Inches(1.0), Inches(4.4)),
        (Inches(6.9), Inches(4.4))
    ]

    for (title, text, color), (x, y) in zip(grid_items, coords):
        card = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, Inches(5.4), Inches(2.3))
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = color
        card.line.width = Pt(1.5)

        tb = s3.shapes.add_textbox(x + Inches(0.3), y + Inches(0.2), Inches(4.8), Inches(1.9))
        tf = tb.text_frame
        tf.word_wrap = True

        p_h = tf.paragraphs[0]
        p_h.text = title
        p_h.font.size = Pt(14)
        p_h.font.bold = True
        p_h.font.color.rgb = color

        p_b = tf.add_paragraph()
        p_b.text = text
        p_b.font.size = Pt(12)
        p_b.font.color.rgb = LIGHT_TEXT
        p_b.space_before = Pt(8)

    # ========================================================
    # SLIDE 4: ML MODEL COMPARISON
    # ========================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_bg(s4)
    add_slide_header(s4, 4, "Machine Learning Model Selection")

    # Table of 4 models
    rows, cols = 5, 4
    table_shape = s4.shapes.add_table(rows, cols, Inches(1.0), Inches(1.8), Inches(11.333), Inches(2.7))
    tbl = table_shape.table

    tbl.columns[0].width = Inches(3.6)
    tbl.columns[1].width = Inches(2.5)
    tbl.columns[2].width = Inches(2.5)
    tbl.columns[3].width = Inches(2.733)

    t_headers = ["Algorithm Tested", "Cross-Validation R²", "Test Accuracy (R²)", "Verdict"]
    for i, h in enumerate(t_headers):
        cell = tbl.cell(0, i)
        cell.text = h
        cell.fill.solid()
        cell.fill.fore_color.rgb = RGBColor(6, 78, 59)
        p = cell.text_frame.paragraphs[0]
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = WHITE

    rows_data = [
        ["1. Linear Regression (Ridge)", "57.8%", "59.6%", "Underfits (Poor for Biology)"],
        ["2. Decision Tree Regressor", "91.2%", "92.4%", "Good Baseline Tree"],
        ["3. Gradient Boosting Regressor", "93.1%", "94.1%", "High Accuracy"],
        ["4. Random Forest Regressor 🏆", "95.9%", "96.8%", "CHAMPION MODEL"]
    ]
    for r_idx, row in enumerate(rows_data):
        for c_idx, val in enumerate(row):
            cell = tbl.cell(r_idx + 1, c_idx)
            cell.text = val
            cell.fill.solid()
            if r_idx == 3:
                cell.fill.fore_color.rgb = RGBColor(16, 78, 59)
            else:
                cell.fill.fore_color.rgb = CARD_BG
            p = cell.text_frame.paragraphs[0]
            p.font.size = Pt(12)
            p.font.color.rgb = EMERALD if r_idx == 3 else LIGHT_TEXT
            if r_idx == 3:
                p.font.bold = True

    # Takeaway Box
    take_card = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(4.8), Inches(11.333), Inches(1.8))
    take_card.fill.solid()
    take_card.fill.fore_color.rgb = CARD_BG
    take_card.line.color.rgb = EMERALD

    tb_tk = s4.shapes.add_textbox(Inches(1.3), Inches(4.9), Inches(10.7), Inches(1.5))
    tf_tk = tb_tk.text_frame
    tf_tk.word_wrap = True

    p = tf_tk.paragraphs[0]
    p.text = "🎯 WHY RANDOM FOREST WON (96.8% ACCURACY):"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = EMERALD

    pts = [
        "Nature is not a straight line: Doubling rain or fertilizer does NOT double crop output.",
        "Random Forest uses 120 decision trees to capture real-world saturating thresholds.",
        "Combined with a log-transform to ensure predictions never return negative yield numbers."
    ]
    for pt in pts:
        p = tf_tk.add_paragraph()
        p.text = f"✔  {pt}"
        p.font.size = Pt(11.5)
        p.font.color.rgb = LIGHT_TEXT
        p.space_before = Pt(4)

    # ========================================================
    # SLIDE 5: 3 KEY SCIENTIFIC FINDINGS
    # ========================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_bg(s5)
    add_slide_header(s5, 5, "3 Key Insights Discovered from the Data")

    finds = [
        ("1. CROP GENETICS DECIDE YIELD",
         "Accounts for 71.8% of prediction importance.\n\nSugarcane naturally yields ~52 tonnes/ha, whereas Wheat and Rice yield 2–4 tonnes/ha.",
         EMERALD),
        ("2. FERTILIZER PARADOX",
         "Fertilizer boosts cash crops (+0.17 for Sugarcane).\n\nBUT too much fertilizer harms pulses (Dal/Moong) because pulses make their own nitrogen!",
         ACCENT_BLUE),
        ("3. RAINFALL LIMIT (2,000 mm)",
         "Rain helps crops up to ~2,000 mm per year.\n\nRain beyond 2,000 mm causes waterlogging and fungal disease, capping maximum crop yield.",
         RGBColor(245, 158, 11))
    ]

    for idx, (title, text, color) in enumerate(finds):
        x = Inches(1.0 + idx * 3.9)
        c = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.8), Inches(3.6), Inches(4.8))
        c.fill.solid()
        c.fill.fore_color.rgb = CARD_BG
        c.line.color.rgb = color
        c.line.width = Pt(1.5)

        tb = s5.shapes.add_textbox(x + Inches(0.2), Inches(2.0), Inches(3.2), Inches(4.4))
        tf = tb.text_frame
        tf.word_wrap = True

        p_t = tf.paragraphs[0]
        p_t.text = title
        p_t.font.size = Pt(13)
        p_t.font.bold = True
        p_t.font.color.rgb = color

        p_b = tf.add_paragraph()
        p_b.text = text
        p_b.font.size = Pt(12)
        p_b.font.color.rgb = LIGHT_TEXT
        p_b.space_before = Pt(14)

    # ========================================================
    # SLIDE 6: WEB APPLICATION & SUMMARY
    # ========================================================
    s6 = prs.slides.add_slide(blank_layout)
    set_bg(s6)
    add_slide_header(s6, 6, "Web Dashboard & Project Conclusion")

    # Left: Technology Stack
    c_stk = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(1.8), Inches(5.4), Inches(4.8))
    c_stk.fill.solid()
    c_stk.fill.fore_color.rgb = CARD_BG
    c_stk.line.color.rgb = EMERALD

    tb_st = s6.shapes.add_textbox(Inches(1.3), Inches(2.0), Inches(4.8), Inches(4.4))
    tf_st = tb_st.text_frame
    tf_st.word_wrap = True

    p = tf_st.paragraphs[0]
    p.text = "💻 TECHNOLOGY STACK"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = EMERALD

    stack_bullets = [
        "Python: Core programming language.",
        "Pandas & NumPy: Data processing & cleaning.",
        "Scikit-Learn: Random Forest machine learning model.",
        "Streamlit: Interactive presentation web dashboard.",
        "Plotly: Interactive comparison charts & trends.",
        "GitHub & Streamlit Cloud: Live 24/7 global hosting."
    ]
    for b in stack_bullets:
        p = tf_st.add_paragraph()
        p.text = f"✔  {b}"
        p.font.size = Pt(12)
        p.font.color.rgb = LIGHT_TEXT
        p.space_before = Pt(9)

    # Right: Farmer-Friendly Output
    c_out = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.9), Inches(1.8), Inches(5.4), Inches(4.8))
    c_out.fill.solid()
    c_out.fill.fore_color.rgb = CARD_BG
    c_out.line.color.rgb = ACCENT_BLUE

    tb_ot = s6.shapes.add_textbox(Inches(7.2), Inches(2.0), Inches(4.8), Inches(4.4))
    tf_ot = tb_ot.text_frame
    tf_ot.word_wrap = True

    p = tf_ot.paragraphs[0]
    p.text = "🌾 SIMPLE OUTPUT FORMAT"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = ACCENT_BLUE

    out_bullets = [
        "Yield per Hectare: (e.g. 4.80 tonnes/ha).",
        "Yield per Acre: (e.g. ~1.94 tonnes/acre) for local farmers.",
        "Total Commercial Output: Total weight for the entire farm.",
        "Commercial Truckloads: (e.g. ≈ 48 ten-tonne trucks) so farmers can easily plan transport."
    ]
    for b in out_bullets:
        p = tf_ot.add_paragraph()
        p.text = f"✔  {b}"
        p.font.size = Pt(12)
        p.font.color.rgb = LIGHT_TEXT
        p.space_before = Pt(11)

    prs.save(PPTX_PATH)
    print("New short, neat presentation generated successfully at:", PPTX_PATH)


if __name__ == "__main__":
    create_clean_presentation()
