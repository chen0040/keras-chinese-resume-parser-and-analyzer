import os
from keras_cn_parser_and_analyzer.library.utility.io_utils import read_pdf, read_pdf_and_docx


def main():
    data_dir_path = './data' # directory to scan for any pdf files
    training_data_dir_path = './data/training_data'
    collected = read_pdf_and_docx(data_dir_path)
    for index, (file_path, file_content) in enumerate(collected.items()):
        with open(os.path.join(training_data_dir_path, str(index) + '.txt'), 'wt', encoding='utf8') as f:
            for line in file_content:
                print(line)
                f.write(line)
                f.write('\n')

    print('count: ', len(collected))


if __name__ == '__main__':
    main()
