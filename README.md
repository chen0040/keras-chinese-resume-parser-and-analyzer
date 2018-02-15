# keras-chinese-resume-parser-and-analyzer

Deep learning project that parses and analyze chinese resumes.

The objective of this project is to use Keras and Deep Learning such as CNN and recurrent neural network to automate the
task of parsing a chinese resume. At the moment the rule-based resume parser has been implemented.

# Overview

### Features 

* Chinese NLP using SnowNLP
* Extract chinese texts using pdfminer.six and python-docx from PDF nad DOCX

# Usage

### Rule-based Chinese Resume Parser

The [sample code](demo/rule_base_parser.py) below shows how to scan all the resumes (in PDF and DOCX formats) from a 
particular directory and print out a summary from the resume parser if information extracted are available:

```python
from keras_cn_parser_and_analyzer.library.rule_based_parser import ResumeParser
from keras_cn_parser_and_analyzer.library.utility.io_utils import read_pdf_and_docx


def main():
    data_dir_path = './data' # directory to scan for any pdf and docx files
    collected = read_pdf_and_docx(data_dir_path, use_ocr=False)
    for file_path, file_content in collected.items():

        print('parsing file: ', file_path)

        parser = ResumeParser()
        parser.parse(file_content)
        print(parser.raw) # print out the raw contents extracted from pdf or docx files

        if parser.unknown is False:
            print(parser.summary())

        print('++++++++++++++++++++++++++++++++++++++++++')

    print('count: ', len(collected))


if __name__ == '__main__':
    main()

```
