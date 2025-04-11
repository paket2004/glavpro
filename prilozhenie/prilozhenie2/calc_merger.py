from docx import Document
from docx.enum.text import WD_BREAK

def merge_docx_with_page_breaks(files, output_file):
    merged_document = Document(files[0])  # Start with the first document

    for file in files[1:]:  # Merge the rest
        # Add page break before next document
        merged_document.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
        
        doc = Document(file)
        for element in doc.element.body:
            merged_document.element.body.append(element)

    merged_document.save(output_file)
    print(f"Documents merged successfully into {output_file} with page breaks")

# Example usage
files_to_merge = ["prilozhenie/prilozhenie2/station.docx", 
                 "prilozhenie/prilozhenie2/moving.docx"]
merge_docx_with_page_breaks(files_to_merge, 
                          "prilozhenie/prilozhenie2/merged_calculations.docx")