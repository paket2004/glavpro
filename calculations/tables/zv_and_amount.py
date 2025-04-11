from docx import Document
from docx.shared import Inches, Pt
from docx.oxml.ns import qn

doc = Document()

style = doc.styles['Normal']
style.font.name = 'Times New Roman'
style.font.size = Pt(6)

section = doc.sections[0]
section._sectPr.xpath('./w:pgSz')[0].set(qn('w:orient'), 'landscape')

# Adjust page width and height for landscape orientation
section.page_width = Inches(11)  # Landscape width (11 inches)
section.page_height = Inches(8.5)  # Landscape height (8.5 inches)
table = doc.add_table(rows=2, cols=9)
table.style = 'Table Grid'

headers = ["Код ЗВ", "Наименование загрязняющего вещества", "ПДК максимальная разовая мг/м3", "ПДК среднесуточная мг/м3", "ПДК среднегодовая мг/м3", "ОБУВ мг/м3",
           "Класс опасности", "Выброс вещества, г/с", "Суммарный выброс вещества, т/год"]

# table.cell(0, 0).merge(table.cell(1, 0))
# table.cell(0, 1).merge(table.cell(1, 1))
# table.cell(0, 2).merge(table.cell(1, 2))
# table.cell(0, 3).merge(table.cell(1, 3))
# table.cell(0, 4).merge(table.cell(1, 4))
# table.cell(0, 5).merge(table.cell(1, 5))
# table.cell(0, 6).merge(table.cell(1, 6))
# table.cell(0, 7).merge(table.cell(1, 7))
# table.cell(0, 8).merge(table.cell(1, 8))


for i, header in enumerate(headers):
    table.cell(0, i).text = header

doc.save("first_table.docx")