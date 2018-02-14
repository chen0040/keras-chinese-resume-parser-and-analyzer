import PyPDF2

def pdf_to_text(pdf_path):
    result = []
    with open(pdf_path, 'rb') as pdfFileObj:
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        for i in range(pdfReader.numPages):
            pageObj = pdfReader.getPage(0)
            result.append(pageObj.extractText())
    return result
