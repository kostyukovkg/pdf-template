from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4") #p-portrait, mm-miillimeters

pdf.add_page() # добавить новую страницу

pdf.set_font(family="Times", style="I", size=14) # this line sets font for the text below
pdf.cell(w=0, h=12, txt="size 14 style I", align='C', ln=1, border=1) # w=0 - cell expands to the end of a page
        # ln - line break: 0 - no break, 1 - break
        # hight = font size
pdf.cell(w=0, h=12, txt="size 14 style I", align='C', ln=1, border=1)

pdf.set_font(family="Times", style="IB", size=10) # new font style is set
pdf.cell(w=0, h=12, txt="size 10 style IB", align='C', ln=1, border=1)

df = pd.read_csv('topics.csv')

pdf.set_font(family="Times", style="B", size=14)
for index, page in df.iterrows():
    pdf.add_page()
    pdf.set_text_color(0,0,254)
    pdf.cell(w=0, h=12, txt=page['Topic'], align='L', ln=1, border=0)
    pdf.line(x1=10, y1=20, x2=200, y2=20) # in mm as we defined before. x- dist from left, y - dist from up

pdf.output("output.pdf")
