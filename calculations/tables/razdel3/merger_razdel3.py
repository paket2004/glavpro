# from docx import Document

# def merge_docx(files, output_file):
#     merged_document = Document(files[0])  # Start with the first document

#     for file in files[1:]:  # Merge the rest
#         doc = Document(file)
#         for element in doc.element.body:
#             merged_document.element.body.append(element)

#     merged_document.save(output_file)
#     print(f"Documents merged successfully into {output_file}")

# # Example usage
# # files_to_merge = ["calculations/tables/razdel3/intro.docx", "calculations/tables/razdel3/3_1.docx", "calculations/tables/razdel3/3_2.docx", "calculations/tables/razdel3/3_6.docx", "calculations/tables/razdel3/3_7.docx", "calculations/tables/razdel3/3_8.docx"]
# files_to_merge = ["calculations/tables/razdel3/intro.docx", "calculations/tables/razdel3/3_1.docx", "calculations/tables/razdel3/3_2.docx", "calculations/tables/razdel3/3_6.docx", "calculations/tables/razdel3/3_7.docx", "calculations/tables/razdel3/3_8.docx"]

# merge_docx(files_to_merge, "calculations/tables/razdel3/razdel3.docx")

from docxcompose.composer import Composer
from docx import Document as Document_compose
from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

def combine_all_docx(filename_master,files_list):
    number_of_sections=len(files_list)
    master = Document_compose(filename_master)
    composer = Composer(master)
    for i in range(0, number_of_sections):
        doc_temp = Document_compose(files_list[i])
        composer.append(doc_temp)
    composer.save(r"calculations\tables\razdel3\razdel3.docx")

files_to_merge = [
    "calculations/tables/razdel3/3_1.docx",
    "calculations/tables/razdel3/3_2.docx", 
    "calculations/tables/razdel3/3_6.docx", 
    "calculations/tables/razdel3/3_7.docx", 
    "calculations/tables/razdel3/3_8.docx"
    ]

filename_master="calculations/tables/razdel3/intro.docx"
# filename_master = "calculations/tables/razdel3/3_1.docx"
combine_all_docx(filename_master,files_to_merge)