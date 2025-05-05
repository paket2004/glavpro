from pypdf import PdfWriter

pdfs = ['prilozhenie\map\intro_pr1.pdf','prilozhenie\map\prilozhenie1.pdf']

merger = PdfWriter()

for pdf in pdfs:
    merger.append(pdf)

merger.write("prilozhenie/map/prilozhenie1_full.pdf")
merger.close()