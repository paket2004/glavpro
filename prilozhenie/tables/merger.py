from docx import Document

def merge_docx(files, output_file):
    merged_document = Document(files[0])  # Start with the first document

    for file in files[1:]:  # Merge the rest
        doc = Document(file)
        for element in doc.element.body:
            merged_document.element.body.append(element)

    merged_document.save(output_file)
    print(f"Documents merged successfully into {output_file}")

# Example usage
files_to_merge = ["prilozhenie/tables/intro_pr4.docx", "prilozhenie/tables/1_1.docx", "prilozhenie/tables/1_2.docx", "prilozhenie/tables/1_3.docx"]
merge_docx(files_to_merge, "prilozhenie/tables/prilozhenie4.docx")
