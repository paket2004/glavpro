from docx import Document
from docx2pdf import convert

def merge_docx_to_pdf(files, output_pdf):
    # First merge to a temporary DOCX
    temp_docx = "temp_merged.docx"
    merged_document = Document(files[0])
    
    for file in files[1:]:
        doc = Document(file)
        for element in doc.element.body:
            merged_document.element.body.append(element)
    
    merged_document.save(temp_docx)
    
    # Convert the temporary DOCX to PDF
    convert(temp_docx, output_pdf)
    print(f"Documents merged successfully into {output_pdf}")

# Example usage
files_to_merge = [
    "prilozhenie/tables/intro_pr4.docx",
    "prilozhenie/tables/1_1.docx",
    "prilozhenie/tables/1_2.docx",
    "prilozhenie/tables/1_3.docx"
]
merge_docx_to_pdf(files_to_merge, "prilozhenie/tables/prilozhenie4.pdf")