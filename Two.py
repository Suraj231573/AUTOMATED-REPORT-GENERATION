import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


file_path = "your_data.csv"  
df = pd.read_csv(' Add your csv file')


summary = df.describe()


pdf_filename = "automated_report.pdf"
pdf = canvas.Canvas(pdf_filename, pagesize=A4)
width, height = A4


pdf.setFont("Helvetica-Bold", 16)
pdf.drawString(50, height - 50, "Automated Report")

pdf.setFont("Helvetica", 12)
y = height - 100


for column in summary.columns:
    pdf.drawString(50, y, f"Column: {column}")
    y -= 20
    for stat in summary.index:
        value = summary.at[stat, column]
        pdf.drawString(70, y, f"{stat}: {value:.2f}")
        y -= 15

        
        if y < 100:
            pdf.showPage()
            pdf.setFont("Helvetica", 12)
            y = height - 100

    y -= 10


pdf.save()
print(f"Report generated successfully: {pdf_filename}")
