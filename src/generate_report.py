from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image,
    Table,
    TableStyle,
    PageBreak
)

OUTPUT_FILE = "report/wage_inflation_research.pdf"

CHART_1 = "charts/chart_1_inflation.png"
CHART_2 = "charts/chart_2_inflation_vs_wages.png"
CHART_3 = "charts/chart_3_real_earnings.png"

doc = SimpleDocTemplate(
    OUTPUT_FILE,
    pagesize=letter,
    rightMargin=50,
    leftMargin=50,
    topMargin=50,
    bottomMargin=50
)

styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    "TitleStyle",
    parent=styles["Title"],
    alignment=TA_CENTER,
    fontSize=22,
    leading=26,
    spaceAfter=18
)

heading_style = ParagraphStyle(
    "HeadingStyle",
    parent=styles["Heading2"],
    fontSize=15,
    leading=18,
    spaceBefore=10,
    spaceAfter=10
)

body_style = ParagraphStyle(
    "BodyStyle",
    parent=styles["BodyText"],
    fontSize=10,
    leading=15,
    spaceAfter=10
)

story = []

story.append(
    Paragraph(
        "Did Wage Growth Keep Pace With Inflation After 2020?",
        title_style
    )
)

story.append(
    Paragraph(
        "A data-driven analysis of U.S. inflation, wage growth, "
        "and real hourly earnings from January 2020 onward.",
        body_style
    )
)

story.append(
    Paragraph(
        "<b>Key finding:</b> Inflation temporarily outpaced wage growth "
        "during the 2021–2022 inflation surge, weakening real hourly "
        "earnings before they later recovered.",
        body_style
    )
)

story.append(
    Paragraph(
        "Data & Methodology",
        heading_style
    )
)

story.append(
    Paragraph(
        "Monthly U.S. data from the Federal Reserve Economic Data (FRED) "
        "were used to compare consumer-price inflation with wage growth "
        "from January 2020 onward. Inflation is measured using the "
        "year-over-year change in CPI, while wage growth is measured using "
        "the year-over-year change in average hourly earnings. Real hourly "
        "earnings are calculated by adjusting nominal earnings using CPI, "
        "with January 2020 set as the baseline (100).",
        body_style
    )
)

story.append(
    Paragraph(
        "<b>Sources:</b> FRED — CPIAUCSL and AHETPI.",
        body_style
    )
)

story.append(Spacer(1, 5))

key_numbers = [
    ["Metric", "Finding"],
    ["Inflation peak", "8.98%"],
    ["Wage growth at peak", "6.58%"],
    ["Wage–inflation gap", "-2.40 percentage points"],
    ["Real earnings low", "101.12"],
    ["January 2020 baseline", "100.00"]
]

key_table = Table(
    key_numbers,
    colWidths=[3.2 * inch, 2.5 * inch]
)

key_table.setStyle(
    TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 0), (-1, -1), 10),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7)
    ])
)

story.append(key_table)
story.append(PageBreak())

story.append(
    Paragraph(
        "1. Inflation Surged",
        heading_style
    )
)

story.append(
    Paragraph(
        "U.S. inflation accelerated sharply after 2020, "
        "reaching a peak of 8.98% year-over-year in June 2022. "
        "The dashed line represents the 2% inflation benchmark.",
        body_style
    )
)

chart_1 = Image(
    CHART_1,
    width=7.0 * inch,
    height=3.5 * inch
)

story.append(chart_1)
story.append(PageBreak())

story.append(
    Paragraph(
        "2. Inflation Outpaced Wage Growth",
        heading_style
    )
)

story.append(
    Paragraph(
        "Wage growth also accelerated after 2020, but it did not keep "
        "pace with inflation during the peak of the surge. In June 2022, "
        "inflation reached 8.98% while wage growth reached 6.58%, "
        "creating a 2.40 percentage-point gap.",
        body_style
    )
)

chart_2 = Image(
    CHART_2,
    width=7.0 * inch,
    height=3.5 * inch
)

story.append(chart_2)
story.append(PageBreak())

story.append(
    Paragraph(
        "3. Real Hourly Earnings Dipped, Then Recovered",
        heading_style
    )
)

story.append(
    Paragraph(
        "Real hourly earnings reached a post-2020 low of 101.12 in June 2022, "
        "using January 2020 as the 100 baseline. Real earnings subsequently "
        "recovered and reached approximately 105–106 by 2026.",
        body_style
    )
)

chart_3 = Image(
    CHART_3,
    width=7.0 * inch,
    height=3.5 * inch
)

story.append(chart_3)

story.append(Spacer(1, 12))

story.append(
    Paragraph(
        "Conclusion",
        heading_style
    )
)

story.append(
    Paragraph(
        "<b>Inflation temporarily outpaced wage growth after 2020, weakening "
        "real purchasing power during the 2021–2022 inflation surge. However, "
        "real hourly earnings later recovered and remained above their "
        "January 2020 level.</b>",
        body_style
    )
)

doc.build(story)

print("PDF generated successfully.")