"""
AgriYield - 2-Page Executive Project Summary PDF Generator
Generates a beautifully styled, simple-English 2-page document explaining:
- The Project Objective
- The Technology Stack
- The Dataset
- Step-by-Step How it Works
- Key Discoveries & Defense Q&A
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

PDF_OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "AgriYield_Project_Explanation.pdf")


class NumberedCanvas(canvas.Canvas):
    """Adds running headers and footers with Page X of Y."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#065f46"))
        
        # Header (Top)
        self.drawString(40, 762, "AgriYield: Data Science-Based Crop Yield Prediction")
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748b"))
        self.drawRightString(572, 762, "Project Overview & Technology Architecture")
        
        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.5)
        self.line(40, 756, 572, 756)
        
        # Footer (Bottom)
        self.line(40, 42, 572, 42)
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748b"))
        self.drawString(40, 30, "Academic Data Science Project | Simple Explanation Guide")
        self.drawRightString(572, 30, f"Page {self._pageNumber} of {page_count}")
        self.restoreState()


def build_pdf():
    doc = SimpleDocTemplate(
        PDF_OUTPUT_PATH,
        pagesize=letter,
        leftMargin=40,
        rightMargin=40,
        topMargin=46,
        bottomMargin=48
    )

    styles = getSampleStyleSheet()
    
    # Custom Typography
    title_style = ParagraphStyle(
        'DocTitle',
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=colors.HexColor('#065f46')
    )
    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        fontName='Helvetica',
        fontSize=9.5,
        leading=13,
        textColor=colors.HexColor('#334155')
    )
    h1_style = ParagraphStyle(
        'Heading1Custom',
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=15,
        textColor=colors.HexColor('#065f46'),
        spaceBefore=7,
        spaceAfter=4
    )
    body_style = ParagraphStyle(
        'BodyCustom',
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor('#1e293b')
    )
    body_bold = ParagraphStyle(
        'BodyBoldCustom',
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor('#0f172a')
    )
    bullet_style = ParagraphStyle(
        'BulletCustom',
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor('#1e293b'),
        leftIndent=12,
        spaceBefore=2,
        spaceAfter=2
    )
    table_cell = ParagraphStyle(
        'TableCell',
        fontName='Helvetica',
        fontSize=8,
        leading=10.5,
        textColor=colors.HexColor('#1e293b')
    )
    table_cell_bold = ParagraphStyle(
        'TableCellBold',
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10.5,
        textColor=colors.HexColor('#065f46')
    )
    box_text = ParagraphStyle(
        'BoxText',
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor('#064e3b')
    )

    story = []

    # ========================================================
    # PAGE 1: OBJECTIVE, STACK & DATASET
    # ========================================================
    story.append(Paragraph("🌾 AgriYield: Crop Yield Prediction System", title_style))
    story.append(Spacer(1, 2))
    story.append(Paragraph("<b>A Complete, Easy-to-Understand Guide to How Our Project Works & What Technologies We Used</b>", subtitle_style))
    story.append(Spacer(1, 6))

    # Highlight Box: The Core Goal
    goal_html = (
        "<b>🎯 The Main Problem We Solved:</b><br/>"
        "Traditionally, farmers and government officials only find out how much crop was harvested <i>after</i> the season ends "
        "by cutting sample fields. This is slow and labor-intensive. <b>AgriYield solves this by using Machine Learning (AI)</b> "
        "to predict harvest output <b>months before harvest</b> using pre-sowing factors like rainfall, fertilizer quantity, farm area, "
        "and crop genetics. This gives early food security warnings and helps farmers plan transport and storage in advance."
    )
    goal_table = Table([[Paragraph(goal_html, box_text)]], colWidths=[532])
    goal_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f0fdf4')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#86efac')),
        ('LINELEFT', (0,0), (-1,-1), 4, colors.HexColor('#10b981')),
        ('PADDING', (0,0), (-1,-1), 7),
    ]))
    story.append(goal_table)
    story.append(Spacer(1, 8))

    # Section 1: Technology Stack
    story.append(Paragraph("1. Technology Stack — What Tools We Used & Why", h1_style))
    story.append(Paragraph("We built this project using a standard, professional Data Science and Python stack. Every tool has a clear purpose:", body_style))
    story.append(Spacer(1, 4))

    stack_data = [
        [
            Paragraph("<b>Component</b>", table_cell_bold),
            Paragraph("<b>Technology Used</b>", table_cell_bold),
            Paragraph("<b>Simple Role in the Project</b>", table_cell_bold)
        ],
        [
            Paragraph("Programming Language", table_cell),
            Paragraph("<b>Python 3.10 / 3.12</b>", table_cell),
            Paragraph("The core language for data science, modeling, calculations, and the web interface.", table_cell)
        ],
        [
            Paragraph("Data Processing", table_cell),
            Paragraph("<b>Pandas & NumPy</b>", table_cell),
            Paragraph("Used to load 19,689 rows of census records, clean missing values, and calculate ratios.", table_cell)
        ],
        [
            Paragraph("Machine Learning Brain", table_cell),
            Paragraph("<b>Scikit-Learn (Random Forest)</b>", table_cell),
            Paragraph("The AI model that studied 24 years of data to learn relationships between weather/soil/inputs and yield.", table_cell)
        ],
        [
            Paragraph("Statistical Validation", table_cell),
            Paragraph("<b>SciPy & Statsmodels</b>", table_cell),
            Paragraph("Conducted ANOVA, Kruskal-Wallis, and correlation tests to scientifically prove relationships.", table_cell)
        ],
        [
            Paragraph("Interactive Dashboard", table_cell),
            Paragraph("<b>Streamlit</b>", table_cell),
            Paragraph("Creates the modern web dashboard interface where users enter farm values and see live predictions.", table_cell)
        ],
        [
            Paragraph("Visual Charts", table_cell),
            Paragraph("<b>Plotly Interactive Charts</b>", table_cell),
            Paragraph("Draws interactive hoverable graphs (crop comparisons, drought trends, and model accuracy).", table_cell)
        ],
        [
            Paragraph("Cloud Deployment", table_cell),
            Paragraph("<b>GitHub & Streamlit Cloud</b>", table_cell),
            Paragraph("Stores project code online and hosts the live website 24/7 for free access from any phone or PC.", table_cell)
        ]
    ]

    stack_table = Table(stack_data, colWidths=[115, 140, 277])
    stack_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#065f46')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e2e8f0')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor('#ffffff'), colors.HexColor('#f8fafc')]),
        ('PADDING', (0,0), (-1,-1), 4.5),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(stack_table)
    story.append(Spacer(1, 8))

    # Section 2: The Dataset
    story.append(Paragraph("2. The Dataset — What Data Did the AI Learn From?", h1_style))
    story.append(Paragraph(
        "We used authentic Indian Agricultural Census records collected over <b>24 years (1997 to 2020)</b> from the "
        "<b>Ministry of Agriculture and Farmers Welfare</b> and rainfall records from the <b>India Meteorological Department (IMD)</b>:",
        body_style
    ))
    story.append(Spacer(1, 3))

    dataset_bullets = [
        "<b>19,689 Real Farm Records:</b> Covering <b>55 distinct crops</b> across <b>30 Indian States and Union Territories</b>.",
        "<b>Inputs Provided to the Model:</b> Crop Species (e.g. Wheat, Rice, Sugarcane), State/Region, Cropping Season (Kharif, Rabi, Whole Year), Cultivated Area (Hectares), Annual Rainfall (mm), Fertilizer Applied (kg), and Pesticide (kg).",
        "<b>Target Variable Predicted:</b> <b>Crop Yield</b>, defined as physical output per unit land: <b>Tonnes per Hectare (t/ha)</b>.",
        "<b>Data Quality:</b> 100% verified complete — 0 duplicate rows, 0 empty missing cells, and strict physical bounds validation."
    ]
    for b in dataset_bullets:
        story.append(Paragraph(f"• {b}", bullet_style))

    # ========================================================
    # PAGE 2: HOW IT WORKS & KEY DISCOVERIES
    # ========================================================
    story.append(PageBreak())

    story.append(Paragraph("3. How the Project Works (Step-by-Step Data Flow)", h1_style))
    story.append(Paragraph("The system follows a strict, reproducible 5-stage Data Science lifecycle:", body_style))
    story.append(Spacer(1, 4))

    workflow_data = [
        [
            Paragraph("<b>Stage</b>", table_cell_bold),
            Paragraph("<b>What Happens Behind the Scenes</b>", table_cell_bold),
            Paragraph("<b>Why It Matters</b>", table_cell_bold)
        ],
        [
            Paragraph("<b>1. Data Audit & Cleaning</b>", table_cell),
            Paragraph("Removes extra spaces, fixes crop spelling variations, validates non-negative inputs, and handles Coconut scale units.", table_cell),
            Paragraph("Prevents typos from creating duplicate categories and corrupting the AI.", table_cell)
        ],
        [
            Paragraph("<b>2. Data Leakage Defense</b>", table_cell),
            Paragraph("<b>Strictly removes 'Total Production'</b> from the input features before training.", table_cell),
            Paragraph("Yield is mathematically Production / Area. If we gave production, the AI would just divide by area instead of learning genuine biology!", table_cell)
        ],
        [
            Paragraph("<b>3. Feature Engineering</b>", table_cell),
            Paragraph("Calculates agronomic intensities: <i>Fertilizer per Hectare</i> and <i>Pesticide per Hectare</i>. Applies log-transforms to skewed metrics.", table_cell),
            Paragraph("Helps the AI compare small family farms (1 ha) and huge district farms (50,000 ha) fairly.", table_cell)
        ],
        [
            Paragraph("<b>4. AI Model Training</b>", table_cell),
            Paragraph("Trained 4 algorithms on historical years (1997–2015) and tested on unseen future years (2016–2020 holdout).", table_cell),
            Paragraph("<b>Random Forest Regressor</b> won with <b>96.8% accuracy (R²)</b> because it handles complex non-linear crop biology.", table_cell)
        ],
        [
            Paragraph("<b>5. Prediction & Presentation</b>", table_cell),
            Paragraph("Takes user inputs from Streamlit, processes through Random Forest, and outputs tonnes/ha, tonnes/acre, and truckload counts.", table_cell),
            Paragraph("Translates technical scientific numbers into practical everyday farming units anyone can understand.", table_cell)
        ]
    ]

    wf_table = Table(workflow_data, colWidths=[105, 235, 192])
    wf_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#065f46')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e2e8f0')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor('#ffffff'), colors.HexColor('#f8fafc')]),
        ('PADDING', (0,0), (-1,-1), 4.5),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(wf_table)
    story.append(Spacer(1, 8))

    # Section 4: Key Discoveries from the Data
    story.append(Paragraph("4. Key Agricultural Discoveries Found by the AI", h1_style))
    story.append(Paragraph("Our data analysis revealed three fascinating real-world facts backed by data:", body_style))
    story.append(Spacer(1, 3))

    findings = [
        "<b>Crop Genetics Form the Yield Ceiling (71.8% Importance):</b> The single most important factor is the crop type itself. Heavy cash crops (Sugarcane ~52 t/ha, Banana ~27 t/ha, Potato ~13 t/ha) naturally produce massive physical tonnage, while cereal grains (Wheat, Rice) yield 2–4 t/ha, and pulses yield ~0.8 t/ha.",
        "<b>Simpson's Paradox in Fertilizer:</b> For cash crops like Sugarcane, adding fertilizer strongly increases yield (+0.17 correlation). But for pulses (like Moong/Gram), adding extra chemical fertilizer actually <i>decreases</i> yield because legume roots naturally create their own nitrogen!",
        "<b>Rainfall Limits & Flooding:</b> Rainfall boosts yield up to approximately 2,000 mm per year. Above 2,000 mm, excess water leads to waterlogging, root rot, and fungal crop damage, capping further yield gains."
    ]
    for f in findings:
        story.append(Paragraph(f"• {f}", bullet_style))

    story.append(Spacer(1, 7))

    # Section 5: Defense Cheat-Sheet
    story.append(Paragraph("5. Quick Q&A for Project Viva / Staff Presentation", h1_style))
    
    qa_html = (
        "<b>Q: What did your model predict?</b><br/>"
        "<b>A:</b> It predicts <i>Crop Yield in Tonnes per Hectare</i>. In our dashboard, we also convert this to <i>Tonnes per Acre</i> and <i>Total Truckloads</i> so that any farmer or executive can immediately understand the output.<br/><br/>"
        "<b>Q: Why did you choose Random Forest over Linear Regression?</b><br/>"
        "<b>A:</b> Linear Regression only scored 59.6% accuracy because nature is not a straight line—doubling rain or fertilizer doesn't double crop yield. Random Forest scored <b>96.8% accuracy</b> because it uses an ensemble of 120 decision trees that capture biological thresholds.<br/><br/>"
        "<b>Q: How did you ensure your model didn't cheat?</b><br/>"
        "<b>A:</b> We strictly enforced zero data leakage: we removed 'Production' before modeling, and we evaluated the model using a strict <i>Temporal Split</i> (trained on past years 1997–2015, tested on unseen future years 2016–2020)."
    )
    qa_table = Table([[Paragraph(qa_html, box_text)]], colWidths=[532])
    qa_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f0fdf4')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#86efac')),
        ('LINELEFT', (0,0), (-1,-1), 4, colors.HexColor('#065f46')),
        ('PADDING', (0,0), (-1,-1), 7),
    ]))
    story.append(qa_table)

    # Build Document using NumberedCanvas
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"PDF successfully built at: {PDF_OUTPUT_PATH}")


if __name__ == "__main__":
    build_pdf()
