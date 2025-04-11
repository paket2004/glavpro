from PyPDF2 import PdfMerger

def merge_pdfs(pdf_files, output_pdf):
    merger = PdfMerger()

    for pdf in pdf_files:
        merger.append(pdf)  # Append each PDF to the merger

    merger.write(output_pdf)  # Save the merged PDF
    merger.close()  # Close the merger to free resources
    print(f"PDFs merged successfully into {output_pdf}")

# Example usage
files_to_merge = [
    "prilozhenie/prilozhenie6/intro_prilozhenie6.pdf",  # Must be PDFs, not DOCX!
    "prilozhenie/prilozhenie6/prilozhenie6.pdf",
]
merge_pdfs(files_to_merge, "prilozhenie/prilozhenie6/merged.pdf")