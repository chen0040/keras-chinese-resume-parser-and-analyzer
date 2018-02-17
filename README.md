# keras-chinese-resume-parser-and-analyzer

Deep learning project that parses and analyze chinese resumes.

The objective of this project is to use Keras and Deep Learning such as CNN and recurrent neural network to automate the
task of parsing a chinese resume. 

### Completed Task:

* At the moment the rule-based resume parser has been implemented.
* Tkinter-based GUI tool to generate and annotate training data from pdf and docx files

### TO-DO List:

* Deep learning multi-class classification using recurrent and cnn networks for
    * line type: classify each line of text extracted from pdf and docx file on whether it is a header, meta-data, or content
    * line label classify each line of text extracted from pdf and docx file on whether it implies experience, education, etc.

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

### Deep Learning: training data generation and annotation

A training data generation and annotation tool is created in the [demo](demo) folder which allows 
resume deep learning training data to be generated from any pdf and docx files stored in the 
[demo/data/resume_samples](demo/data/resume_samples) folder, To launch this tool, run the following 
command from the root directory of the project:

```batch
cd demo
python create_training_data.py
``` 

This will parse the pdf and docx files in [demo/data/resume_samples](demo/data/resume_samples) folder
and for each of these file launch a Tkinter-based GUI form to user to annotate individual text line
in the pdf or docx file (clicking the "Type: ..." and "Label: ..." buttons multiple time to select the 
correct annotation for each line). On each form closing, the generated and annotated data will be saved
to a text file in the [demo/data/training_data](demo/data/training_data) folder.  each line in the
text file will have the following format

```text
line_type   line_label  line_content
```

line_type and line_label has the following mapping to the actual class labels

```python
line_labels = {0: 'experience', 1: 'knowledge', 2: 'education', 3: 'project', 4: 'others'}
line_types = {0: 'header', 1: 'meta', 2: 'content'}
```
