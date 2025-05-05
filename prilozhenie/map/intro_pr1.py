from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx2pdf import convert

def generate_intro_pr1(output_pdf):
    doc = Document()

    # Add a centered title
    title = doc.add_paragraph('''
   Карта-схема расположения источников выбросов загрязняющих
    веществ в атмосферу
    Муниципальное бюджетное общеобразовательное учреждение
    «Мирошкинская средняя общеобразовательная школа»
    Первомайского района Оренбургской области
    (МБОУ «Мирошкинская СОШ»)''')
    title.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    title.runs[0].bold = True
    title.runs[0].font.size = Pt(14)
    temp_docx = "emissions_report.docx"
    doc.save(temp_docx)
    convert(temp_docx, output_pdf)
    print(f"PDF generated successfully: {output_pdf}")
# Example usage
generate_intro_pr1("prilozhenie/map/intro_pr1.pdf")