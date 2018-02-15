from keras_cn_parser_and_analyzer.library.utility.io_utils import read_pdf_and_docx
from keras_cn_parser_and_analyzer.library.utility.nlp_utils import print_snow


def main():
    data_dir_path = '../data'
    collected = read_pdf_and_docx(data_dir_path)
    for file_path, file_content in collected.items():
        print('file: ', file_path)
        for i in range(len(file_content)):
            line = file_content[i]
            if len(line) > 10:
                print_snow(line)

    print('count: ', len(collected))


if __name__ == '__main__':
    main()
