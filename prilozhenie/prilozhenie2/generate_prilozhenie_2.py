import os
from PyPDF2 import PdfMerger
from docx2pdf import convert  # Requires `docx2pdf` (pip install docx2pdf)

def merge_pdf_docx(pdf_path, docx_path, output_pdf_path):
    """Merge a PDF and DOCX into a single PDF."""
    try:
        # Temporary PDF for the DOCX content
        temp_pdf_path = "prilozhenie/prilozhenie2/temp_docx.pdf"
        
        # 1. Convert DOCX to PDF
        convert(docx_path, temp_pdf_path)  # Using docx2pdf
        
        # 2. Merge both PDFs
        merger = PdfMerger()
        merger.append(pdf_path)      # Original PDF
        merger.append(temp_pdf_path) # DOCX-as-PDF
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

# Usage
merge_pdf_docx(
    pdf_path="C:/Users/79133/glavpro/prilozhenie/prilozhenie2/result.pdf",
    docx_path="C:/Users/79133/glavpro/prilozhenie/prilozhenie2/merged_calculations.docx",
    output_pdf_path="C:/Users/79133/glavpro/prilozhenie/prilozhenie2/merged_final.pdf"
)