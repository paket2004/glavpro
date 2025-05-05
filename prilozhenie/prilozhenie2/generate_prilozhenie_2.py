import os
from PyPDF2 import PdfMerger
from docx2pdf import convert

def merge_pdf_docx(pdf_path, docx_path, output_pdf_path):
    """Merge a PDF and DOCX into a single PDF."""
    try:
        # Temporary PDF for the DOCX content
        temp_pdf_path = "prilozhenie/prilozhenie2/temp_docx.pdf"
        
        convert(docx_path, temp_pdf_path)
        merger = PdfMerger()
        merger.append(pdf_path)
        merger.append(temp_pdf_path)
        merger.write(output_pdf_path)
        merger.close()
        
        # Cleanup
        os.remove(temp_pdf_path)
        print(f"Merged PDF saved to: {output_pdf_path}")
        return True
    
    except Exception as e:
        print(f"Error: {str(e)}")
        if os.path.exists(temp_pdf_path):
            os.remove(temp_pdf_path)
        return False

merge_pdf_docx(
    pdf_path="prilozhenie/prilozhenie2/prilozhenie2.pdf",
    docx_path="prilozhenie/prilozhenie2/car_report.docx",
    output_pdf_path="prilozhenie/prilozhenie2/part_2.pdf"
)