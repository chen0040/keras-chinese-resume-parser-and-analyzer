import docx


def docx_to_text(file_path):
    doc = docx.Document(file_path)
    result = []
    for p in doc.paragraphs:
        result.append(p.text)
    return result
