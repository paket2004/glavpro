from pypdf import PdfWriter

pdfs = ['prilozhenie/prilozhenie2/0001.pdf', 'prilozhenie/prilozhenie2/0002.pdf']

merger = PdfWriter()

for pdf in pdfs:
    merger.append(pdf)

merger.write("prilozhenie/prilozhenie2/result.pdf")
merger.close()