from PyPDF2 import PdfMerger

def merge_pdfs(pdf_files, output_pdf):
    merger = PdfMerger()
    for pdf in pdf_files:
        merger.append(pdf)
    merger.write(output_pdf)
    merger.close()
    print(f"PDFs merged successfully into {output_pdf}")
files_to_merge = [
    r"prilozhenie/map/prilozhenie1_full.pdf", 
    r"prilozhenie/prilozhenie2/part_2.pdf",
    r"prilozhenie/prilozhenie3/prilozhenie3.pdf",
    r"prilozhenie/tables/prilozhenie4.pdf",
    r"prilozhenie/prilozhenie5/prilozhenie5.pdf",
    r"prilozhenie/prilozhenie6/merged.pdf"
]
merge_pdfs(files_to_merge, "prilozhenie/prilozhenie.pdf")