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
    "prilozhenie/prilozhenie2/merged_final.pdf",  # Must be PDFs, not DOCX!
    "prilozhenie/prilozhenie3/prilozhenie3.pdf",
    "prilozhenie/tables/prilozhenie4.pdf",
    "prilozhenie/prilozhenie5/prilozhenie5.pdf",
    "prilozhenie/prilozhenie6/merged.pdf"
]
merge_pdfs(files_to_merge, "prilozhenie/prilozhenie.pdf")