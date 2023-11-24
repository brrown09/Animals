import pandas as pd
import pdfkit
from fpdf import FPDF
import glob
from pathlib import Path
from pdfkit import from_string

filepaths = glob.glob("Pets/*.txt")
pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    pdf.add_page()
    page_title = Path(filepath).stem
    pdf.set_font(style="B", family="Times", size=16)
    pdf.cell(w=30, h=8, txt=f"{page_title.capitalize()}", ln=1)
    with open(filepath) as file:
        content = file.read()
        pdf.set_font(style="", family="Times", size=12)
        pdf.multi_cell(w=194, h=5, fill=False, txt=str(content), border=0 )

pdf.output("Animals.pdf")
