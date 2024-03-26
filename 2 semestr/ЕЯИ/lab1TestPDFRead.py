import PyPDF2

pdfFile = open("Industrial Society and Its Future.pdf", "rb")

pdfReader = PyPDF2.PdfReader(pdfFile)


for page in pdfReader.pages:
    with open ("C:\\work\\2 semestr\\ЕЯИ\\test.txt", "a") as file:
        file.write(page.extract_text())

pdfFile.close()