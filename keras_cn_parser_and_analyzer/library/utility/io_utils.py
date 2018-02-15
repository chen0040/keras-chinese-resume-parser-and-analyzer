import os
from keras_cn_parser_and_analyzer.library.utility.pdf_utils import pdf_to_text
from keras_cn_parser_and_analyzer.library.utility.docx_utils import docx_to_text


def read_pdf_and_docx(dir_path, collected=None):
    if collected is None:
        collected = dict()
    for f in os.listdir(dir_path):
        file_path = os.path.join(dir_path, f)
        if os.path.isfile(file_path):
            txt = None
            if f.lower().endswith('.docx'):
                txt = docx_to_text(file_path)
            elif f.lower().endswith('.pdf'):
                txt = pdf_to_text(file_path)
            if txt is not None and len(txt) > 0:
                collected[file_path] = txt
        elif os.path.isdir(file_path):
            read_pdf_and_docx(file_path, collected)

    return collected
