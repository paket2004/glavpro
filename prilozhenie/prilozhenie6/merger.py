from PyPDF2 import PdfMerger

def merge_pdfs(pdf_files, output_pdf):
    merger = PdfMerger()

    for pdf in pdf_files:
        merger.append(pdf)

    merger.write(output_pdf)
    merger.close()
    print(f"PDFs merged successfully into {output_pdf}")
files_to_merge = [
    "prilozhenie/prilozhenie6/intro_prilozhenie6.pdf", 
    "prilozhenie/prilozhenie6/prilozhenie6.pdf",
]
merge_pdfs(files_to_merge, "prilozhenie/prilozhenie6/merged.pdf")