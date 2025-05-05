from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx2pdf import convert

def generate_emissions_report(output_pdf):
    doc = Document()
    title = doc.add_paragraph('''
    CПРАВОЧНОЕ''')
    title.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    title.runs[0].bold = True
    title.runs[0].font.size = Pt(14)
    temp_docx = "emissions_report.docx"
    doc.save(temp_docx)
    convert(temp_docx, output_pdf)
    print(f"PDF generated successfully: {output_pdf}")
generate_emissions_report("prilozhenie/prilozhenie6/intro_prilozhenie6.pdf")