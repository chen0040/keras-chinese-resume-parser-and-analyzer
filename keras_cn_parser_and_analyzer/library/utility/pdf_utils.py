import PyPDF2

from keras_cn_parser_and_analyzer.library.utility.text_utils import preprocess_text


def pdf_to_text(pdf_path):
    result = []
    with open(pdf_path, 'rb') as pdfFileObj:
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        for i in range(pdfReader.numPages):
            pageObj = pdfReader.getPage(0)
            txt = pageObj.extractText().strip()
            if txt != '':
                txt = preprocess_text(txt)
                result.append(txt)
    return result
