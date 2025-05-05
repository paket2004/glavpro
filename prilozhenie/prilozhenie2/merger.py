from pypdf import PdfWriter

pdfs = ['prilozhenie\prilozhenie2\intro_pr2.pdf','prilozhenie/prilozhenie2/0001.pdf', 'prilozhenie/prilozhenie2/0002.pdf']

merger = PdfWriter()

for pdf in pdfs:
    merger.append(pdf)

merger.write("prilozhenie/prilozhenie2/prilozhenie2.pdf")
merger.close()