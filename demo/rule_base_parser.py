from keras_cn_parser_and_analyzer.library.parser import ResumeParser
from keras_cn_parser_and_analyzer.library.utility.io_utils import read_pdf_and_docx


def main():
    data_dir_path = './data' # directory to scan for any pdf and docx files
    collected = read_pdf_and_docx(data_dir_path)
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
