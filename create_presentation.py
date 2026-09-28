"""
AgriYield - High-Impact Light-Theme Presentation Generator (6 Slides)
Designed specifically for college projectors / viva presentations:
- Crisp Light Theme (White / Slate / Emerald)
- Big, readable fonts (titles 28-36pt, bodies 15-18pt)
- No broken emojis (uses clean typography and bullet marks)
- S. SANDHIYA (ROLL NO : 24VNM034) prominently featured
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

PPTX_PATH = os.path.join(os.path.dirname(__file__), "AgriYield_Presentation.pptx")

# Light Theme Palette
BG_COLOR = RGBColor(248, 250, 252)       # Crisp soft off-white #f8fafc
WHITE = RGBColor(255, 255, 255)          # Card background #ffffff
CARD_BORDER = RGBColor(226, 232, 240)    # Soft gray border #e2e8f0
CARD_BG_GREEN = RGBColor(240, 253, 244)  # Light mint tint #f0fdf4
CARD_BG_RED = RGBColor(254, 242, 242)    # Light red tint #fef2f2

PRIMARY_DARK = RGBColor(15, 23, 42)      # Deep slate for main text #0f172a
BODY_MUTED = RGBColor(51, 65, 85)        # Readable dark slate #334155
EMERALD = RGBColor(5, 150, 105)          # Forest emerald #059669
EMERALD_DARK = RGBColor(6, 95, 70)       # Deep forest #065f46
ACCENT_BLUE = RGBColor(2, 132, 199)      # Sky blue #0284c7
ACCENT_RED = RGBColor(220, 38, 38)       # Crimson red #dc2626
ACCENT_PURPLE = RGBColor(124, 58, 237)   # Purple #7c3aed
ACCENT_AMBER = RGBColor(217, 119, 6)     # Amber #d97706


def set_slide_bg(slide):
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = BG_COLOR


def add_slide_header(slide, slide_num, title):
    # Top Tag
    tag_box = slide.shapes.add_textbox(Inches(0.9), Inches(0.4), Inches(11.5), Inches(0.35))
    p_tag = tag_box.text_frame.paragraphs[0]
    p_tag.text = f"AGRIYIELD  •  SLIDE {slide_num} OF 6"
    p_tag.font.size = Pt(11)
    p_tag.font.bold = True
    p_tag.font.color.rgb = EMERALD

    # Slide Title
    t_box = slide.shapes.add_textbox(Inches(0.9), Inches(0.7), Inches(11.5), Inches(0.8))
    p_title = t_box.text_frame.paragraphs[0]
    p_title.text = title
    p_title.font.size = Pt(28)
    p_title.font.bold = True
    p_title.font.color.rgb = PRIMARY_DARK


def create_light_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # ========================================================
    # SLIDE 1: COVER SLIDE
    # ========================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s1)

    # Top emerald banner strip
    banner = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.9), Inches(0.8), Inches(11.533), Inches(0.12))
    banner.fill.solid()
    banner.fill.fore_color.rgb = EMERALD
    banner.line.color.rgb = EMERALD

    # Main Project Title
    t_box = s1.shapes.add_textbox(Inches(0.9), Inches(1.15), Inches(11.533), Inches(1.8))
    tf1 = t_box.text_frame
    tf1.word_wrap = True
    
    p1 = tf1.paragraphs[0]
    p1.text = "AgriYield: Crop Yield Prediction System"
    p1.font.size = Pt(36)
    p1.font.bold = True
    p1.font.color.rgb = EMERALD_DARK

    p1_sub = tf1.add_paragraph()
    p1_sub.text = "Data Science-Based Agricultural Analysis & Pre-Harvest Machine Learning Forecasting"
    p1_sub.font.size = Pt(18)
    p1_sub.font.color.rgb = BODY_MUTED
    p1_sub.space_before = Pt(6)

    # Presenter Card (Prominent Left Box)
    auth_card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.9), Inches(3.2), Inches(6.0), Inches(3.6))
    auth_card.fill.solid()
    auth_card.fill.fore_color.rgb = CARD_BG_GREEN
    auth_card.line.color.rgb = EMERALD
    auth_card.line.width = Pt(2.5)

    at_box = s1.shapes.add_textbox(Inches(1.2), Inches(3.45), Inches(5.4), Inches(3.1))
    at_tf = at_box.text_frame
    at_tf.word_wrap = True
    
    p_a1 = at_tf.paragraphs[0]
    p_a1.text = "PROJECT PRESENTED BY"
    p_a1.font.size = Pt(13)
    p_a1.font.bold = True
    p_a1.font.color.rgb = EMERALD

    p_a2 = at_tf.add_paragraph()
    p_a2.text = "S. SANDHIYA"
    p_a2.font.size = Pt(34)
    p_a2.font.bold = True
    p_a2.font.color.rgb = PRIMARY_DARK
    p_a2.space_before = Pt(8)

    p_a3 = at_tf.add_paragraph()
    p_a3.text = "ROLL NO : 24VNM034"
    p_a3.font.size = Pt(20)
    p_a3.font.bold = True
    p_a3.font.color.rgb = ACCENT_BLUE
    p_a3.space_before = Pt(8)

    p_a4 = at_tf.add_paragraph()
    p_a4.text = "Data Science & Machine Learning Investigation"
    p_a4.font.size = Pt(14)
    p_a4.font.color.rgb = BODY_MUTED
    p_a4.space_before = Pt(8)

    # Project Scope Card (Right Box)
    info_card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.2), Inches(3.2), Inches(5.2), Inches(3.6))
    info_card.fill.solid()
    info_card.fill.fore_color.rgb = WHITE
    info_card.line.color.rgb = CARD_BORDER
    info_card.line.width = Pt(1.5)

    it_box = s1.shapes.add_textbox(Inches(7.5), Inches(3.45), Inches(4.6), Inches(3.1))
    it_tf = it_box.text_frame
    it_tf.word_wrap = True
    
    p_i1 = it_tf.paragraphs[0]
    p_i1.text = "KEY PROJECT HIGHLIGHTS"
    p_i1.font.size = Pt(13)
    p_i1.font.bold = True
    p_i1.font.color.rgb = EMERALD

    facts = [
        "19,689 Real Census Records (1997–2020)",
        "55 Crops & 30 Indian States Nationwide",
        "Champion Model: Random Forest Regressor",
        "Predictive Accuracy: 96.8% (R² Score)",
        "Zero Data Leakage: Genuine Pre-Harvest ML"
    ]
    for f in facts:
        p = it_tf.add_paragraph()
        p.text = f"•  {f}"
        p.font.size = Pt(14.5)
        p.font.bold = True
        p.font.color.rgb = PRIMARY_DARK
        p.space_before = Pt(8)

    # ========================================================
    # SLIDE 2: THE REAL-WORLD PROBLEM & SOLUTION
    # ========================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s2)
    add_slide_header(s2, 2, "The Real-World Problem & Our Solution")

    # Left: The Traditional Problem
    c_prob = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.9), Inches(1.6), Inches(5.6), Inches(5.3))
    c_prob.fill.solid()
    c_prob.fill.fore_color.rgb = CARD_BG_RED
    c_prob.line.color.rgb = ACCENT_RED
    c_prob.line.width = Pt(2)

    tb_p = s2.shapes.add_textbox(Inches(1.2), Inches(1.9), Inches(5.0), Inches(4.7))
    tf_p = tb_p.text_frame
    tf_p.word_wrap = True

    p = tf_p.paragraphs[0]
    p.text = "THE PROBLEM TODAY"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = ACCENT_RED

    prob_items = [
        ("Post-Harvest Delay: ", "Yield is only measured after harvesting is completely finished through slow manual crop-cutting."),
        ("Too Late for Action: ", "When food shortages occur, prices have already spiked and inflation has hurt citizens."),
        ("No Advance Planning: ", "Farmers and transport operators cannot plan trucks, storage, or sales months in advance.")
    ]
    for title, desc in prob_items:
        p = tf_p.add_paragraph()
        p.text = f"• {title}{desc}"
        p.font.size = Pt(15.5)
        p.font.color.rgb = PRIMARY_DARK
        p.space_before = Pt(16)

    # Right: The AgriYield Solution
    c_sol = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.6), Inches(5.6), Inches(5.3))
    c_sol.fill.solid()
    c_sol.fill.fore_color.rgb = CARD_BG_GREEN
    c_sol.line.color.rgb = EMERALD
    c_sol.line.width = Pt(2)

    tb_s = s2.shapes.add_textbox(Inches(7.1), Inches(1.9), Inches(5.0), Inches(4.7))
    tf_s = tb_s.text_frame
    tf_s.word_wrap = True

    p = tf_s.paragraphs[0]
    p.text = "THE AGRIYIELD SOLUTION"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = EMERALD

    sol_items = [
        ("Pre-Harvest AI Forecasting: ", "Predicts crop harvest months in advance using data available during planting season."),
        ("Practical Input Factors: ", "Uses annual rainfall, fertilizer amount, pesticide, land area, and crop genetics."),
        ("Farmer-Friendly Outputs: ", "Translates mathematical yield into practical tonnes per acre and commercial truckload counts.")
    ]
    for title, desc in sol_items:
        p = tf_s.add_paragraph()
        p.text = f"• {title}{desc}"
        p.font.size = Pt(15.5)
        p.font.color.rgb = PRIMARY_DARK
        p.space_before = Pt(16)

    # ========================================================
    # SLIDE 3: DATASET & DATA LEAKAGE DEFENSE
    # ========================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s3)
    add_slide_header(s3, 3, "Dataset Scope & Zero Data Leakage")

    grid = [
        ("19,689 Records", "24 Years of official Indian farm census records (1997 to 2020) collected from the Ministry of Agriculture & IMD.", EMERALD),
        ("55 Crops & 30 States", "Wide coverage across food grains (Rice, Wheat), pulses (Gram, Moong), oilseeds, and heavy cash crops (Sugarcane).", ACCENT_BLUE),
        ("Zero Data Leakage Protocol", "Strictly excluded 'Total Production' because Yield = Production / Area. If included, the AI would cheat by dividing instead of predicting.", ACCENT_PURPLE),
        ("Real Future Holdout Testing", "Trained on historical years (1997–2015, 15,404 rows) and tested on unseen future years (2016–2020, 4,285 rows).", ACCENT_AMBER)
    ]

    coords = [
        (Inches(0.9), Inches(1.6)),
        (Inches(6.8), Inches(1.6)),
        (Inches(0.9), Inches(4.3)),
        (Inches(6.8), Inches(4.3))
    ]

    for (title, text, color), (x, y) in zip(grid, coords):
        card = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, Inches(5.6), Inches(2.5))
        card.fill.solid()
        card.fill.fore_color.rgb = WHITE
        card.line.color.rgb = color
        card.line.width = Pt(2)

        tb = s3.shapes.add_textbox(x + Inches(0.3), y + Inches(0.2), Inches(5.0), Inches(2.1))
        tf = tb.text_frame
        tf.word_wrap = True

        p_h = tf.paragraphs[0]
        p_h.text = title
        p_h.font.size = Pt(18)
        p_h.font.bold = True
        p_h.font.color.rgb = color

        p_b = tf.add_paragraph()
        p_b.text = text
        p_b.font.size = Pt(15)
        p_b.font.color.rgb = PRIMARY_DARK
        p_b.space_before = Pt(8)

    # ========================================================
    # SLIDE 4: ML MODEL COMPARISON
    # ========================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s4)
    add_slide_header(s4, 4, "Machine Learning Model Selection")

    # Table of 4 models
    rows, cols = 5, 4
    table_shape = s4.shapes.add_table(rows, cols, Inches(0.9), Inches(1.6), Inches(11.533), Inches(2.9))
    tbl = table_shape.table

    tbl.columns[0].width = Inches(3.8)
    tbl.columns[1].width = Inches(2.5)
    tbl.columns[2].width = Inches(2.5)
    tbl.columns[3].width = Inches(2.733)

    t_headers = ["Algorithm Tested", "5-Fold CV R²", "Holdout Test R²", "Status & Verdict"]
    for i, h in enumerate(t_headers):
        cell = tbl.cell(0, i)
        cell.text = h
        cell.fill.solid()
        cell.fill.fore_color.rgb = EMERALD_DARK
        p = cell.text_frame.paragraphs[0]
        p.font.size = Pt(15)
        p.font.bold = True
        p.font.color.rgb = WHITE

    rows_data = [
        ["1. Linear Regression (Ridge)", "57.8%", "59.6%", "Underfits (Poor for Biology)"],
        ["2. Decision Tree Regressor", "91.2%", "92.4%", "Good Baseline Tree"],
        ["3. Gradient Boosting Regressor", "93.1%", "94.1%", "Strong Non-Linear Fit"],
        ["4. Random Forest Regressor", "95.9%", "96.8%", "CHAMPION MODEL (Winner)"]
    ]
    for r_idx, row in enumerate(rows_data):
        for c_idx, val in enumerate(row):
            cell = tbl.cell(r_idx + 1, c_idx)
            cell.text = val
            cell.fill.solid()
            if r_idx == 3:
                cell.fill.fore_color.rgb = CARD_BG_GREEN
            else:
                cell.fill.fore_color.rgb = WHITE
            p = cell.text_frame.paragraphs[0]
            p.font.size = Pt(15)
            p.font.color.rgb = EMERALD_DARK if r_idx == 3 else PRIMARY_DARK
            if r_idx == 3:
                p.font.bold = True

    # Takeaway Box
    take_card = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.9), Inches(4.8), Inches(11.533), Inches(2.1))
    take_card.fill.solid()
    take_card.fill.fore_color.rgb = WHITE
    take_card.line.color.rgb = EMERALD
    take_card.line.width = Pt(2)

    tb_tk = s4.shapes.add_textbox(Inches(1.2), Inches(4.95), Inches(10.9), Inches(1.8))
    tf_tk = tb_tk.text_frame
    tf_tk.word_wrap = True

    p = tf_tk.paragraphs[0]
    p.text = "WHY RANDOM FOREST WON (96.8% ACCURACY):"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = EMERALD_DARK

    pts = [
        "Nature is not a straight line: Doubling rain or fertilizer does NOT double crop output.",
        "Random Forest uses 120 decision trees to capture real-world saturating biological limits.",
        "Combined with a target log-transform (ln(1+y)) to guarantee positive yield predictions."
    ]
    for pt in pts:
        p = tf_tk.add_paragraph()
        p.text = f"•  {pt}"
        p.font.size = Pt(15)
        p.font.color.rgb = PRIMARY_DARK
        p.space_before = Pt(6)

    # ========================================================
    # SLIDE 5: 3 KEY SCIENTIFIC DISCOVERIES
    # ========================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s5)
    add_slide_header(s5, 5, "3 Key Insights Discovered from the Data")

    finds = [
        ("1. CROP GENETICS DECIDE YIELD",
         "Accounts for 71.8% of prediction importance.\n\nSugarcane naturally yields ~52 tonnes/ha, whereas Wheat and Rice yield 2–4 tonnes/ha.",
         EMERALD),
        ("2. THE FERTILIZER PARADOX",
         "Fertilizer boosts cash crops (+0.17 for Sugarcane).\n\nBUT excess chemical fertilizer hurts pulses (Moong/Gram) because pulses naturally fix nitrogen!",
         ACCENT_BLUE),
        ("3. RAINFALL LIMIT (2,000 mm)",
         "Rain boosts crop yield up to ~2,000 mm per year.\n\nBeyond 2,000 mm, waterlogging, root rot, and fungal disease cap maximum crop productivity.",
         ACCENT_AMBER)
    ]

    for idx, (title, text, color) in enumerate(finds):
        x = Inches(0.9 + idx * 3.9)
        c = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.6), Inches(3.7), Inches(5.3))
        c.fill.solid()
        c.fill.fore_color.rgb = WHITE
        c.line.color.rgb = color
        c.line.width = Pt(2)

        tb = s5.shapes.add_textbox(x + Inches(0.25), Inches(1.9), Inches(3.2), Inches(4.7))
        tf = tb.text_frame
        tf.word_wrap = True

        p_t = tf.paragraphs[0]
        p_t.text = title
        p_t.font.size = Pt(17)
        p_t.font.bold = True
        p_t.font.color.rgb = color

        p_b = tf.add_paragraph()
        p_b.text = text
        p_b.font.size = Pt(15.5)
        p_b.font.color.rgb = PRIMARY_DARK
        p_b.space_before = Pt(16)

    # ========================================================
    # SLIDE 6: WEB APPLICATION & OUTPUT
    # ========================================================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s6)
    add_slide_header(s6, 6, "Web Dashboard & Implementation")

    # Left: Technology Stack
    c_stk = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.9), Inches(1.6), Inches(5.6), Inches(5.3))
    c_stk.fill.solid()
    c_stk.fill.fore_color.rgb = WHITE
    c_stk.line.color.rgb = EMERALD
    c_stk.line.width = Pt(2)

    tb_st = s6.shapes.add_textbox(Inches(1.2), Inches(1.9), Inches(5.0), Inches(4.7))
    tf_st = tb_st.text_frame
    tf_st.word_wrap = True

    p = tf_st.paragraphs[0]
    p.text = "TECHNOLOGY STACK"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = EMERALD

    stack_bullets = [
        ("Python: ", "Core programming language for data science."),
        ("Pandas & NumPy: ", "Data cleaning and preprocessing."),
        ("Scikit-Learn: ", "Random Forest machine learning model."),
        ("Streamlit: ", "Interactive presentation web dashboard."),
        ("Plotly: ", "Interactive charts, trends, and comparisons."),
        ("GitHub & Streamlit Cloud: ", "24/7 online hosting.")
    ]
    for tool, desc in stack_bullets:
        p = tf_st.add_paragraph()
        p.text = f"• {tool}{desc}"
        p.font.size = Pt(15)
        p.font.color.rgb = PRIMARY_DARK
        p.space_before = Pt(12)

    # Right: Farmer-Friendly Output
    c_out = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.6), Inches(5.6), Inches(5.3))
    c_out.fill.solid()
    c_out.fill.fore_color.rgb = WHITE
    c_out.line.color.rgb = ACCENT_BLUE
    c_out.line.width = Pt(2)

    tb_ot = s6.shapes.add_textbox(Inches(7.1), Inches(1.9), Inches(5.0), Inches(4.7))
    tf_ot = tb_ot.text_frame
    tf_ot.word_wrap = True

    p = tf_ot.paragraphs[0]
    p.text = "SIMPLE OUTPUT FORMAT"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = ACCENT_BLUE

    out_bullets = [
        ("Yield per Hectare: ", "Scientific standard unit (e.g. 4.80 t/ha)."),
        ("Yield per Acre: ", "Practical measure for local farmers (e.g. ~1.94 t/acre)."),
        ("Total Farm Harvest: ", "Total gross tonnage expected from the entire field."),
        ("Commercial Truckloads: ", "Estimated count of 10-tonne trucks (e.g. ≈ 48 trucks) so transport is planned easily.")
    ]
    for unit, desc in out_bullets:
        p = tf_ot.add_paragraph()
        p.text = f"• {unit}{desc}"
        p.font.size = Pt(15)
        p.font.color.rgb = PRIMARY_DARK
        p.space_before = Pt(14)

    prs.save(PPTX_PATH)
    print("New high-impact LIGHT THEME presentation saved at:", PPTX_PATH)


if __name__ == "__main__":
    create_light_presentation()
