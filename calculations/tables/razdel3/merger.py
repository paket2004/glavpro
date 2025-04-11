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
files_to_merge = ["calculations/tables/razdel3/intro.docx", "calculations/tables/razdel3/test_3_1.docx", "calculations/tables/razdel3/test_3_2.docx", "calculations/tables/razdel3/3_6.docx", "calculations/tables/razdel3/test_3_7.docx", "calculations/tables/razdel3/test_3_8.docx"]
merge_docx(files_to_merge, "calculations/tables/razdel3/merged_output.docx")
