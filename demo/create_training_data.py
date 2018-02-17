import os
from keras_cn_parser_and_analyzer.library.utility.io_utils import read_pdf, read_pdf_and_docx

def main():
    data_dir_path = './data'  # directory to scan for any pdf files
    training_data_dir_path = './data/training_data'
    collected = read_pdf_and_docx(data_dir_path, command_logging=True)
    for index, (file_path, file_content) in enumerate(collected.items()):
        with open(os.path.join(training_data_dir_path, str(index) + '.txt'), 'wt', encoding='utf8') as f:
            for line_index, line in enumerate(file_content):
                print('Line #' + str(line_index) + ': ', line)
                label = input('Label for line #' + str(line_index) + ' (options: 0=header 1=meta 2=expertise 3=job_scope 4=others)')
                f.write(label + '\t' + line)
                f.write('\n')

    print('count: ', len(collected))


if __name__ == '__main__':
    main()
