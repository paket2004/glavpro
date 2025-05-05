from docxcompose.composer import Composer
from docx import Document as Document_compose
from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

def add_page_break(doc):
    """Inserts a page break into the document."""
    paragraph = doc.add_paragraph()
    run = paragraph.add_run()
    br = OxmlElement('w:br')
    br.set(qn('w:type'), 'page')
    run._r.append(br)

def combine_all_docx(filename_master,files_list):
    number_of_sections=len(files_list)
    master = Document_compose(filename_master)
    composer = Composer(master)
    for i in range(0, number_of_sections):
        doc_temp = Document_compose(files_list[i])
        composer.append(doc_temp)
        # if i < len(files_list) - 1:
        #     add_page_break(composer.doc)
        
    composer.save(r"inventarization_description\izav_info\razdel2.docx")

filename_master = "inventarization_description/izav_info/description.docx"
files_to_merge = [
    "inventarization_description/izav_info/part2_without_intro.docx"
]

combine_all_docx(filename_master, files_to_merge)
