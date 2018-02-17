import os
from keras_cn_parser_and_analyzer.library.utility.io_utils import read_pdf, read_pdf_and_docx
from tkinter import *


class AnnotatorGui(Frame):
    def __init__(self, file_content):
        Frame.__init__(self)
        self.master.title("Annotate Resume Lines")

        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=W + E + N + S)

        self.line_index_label_list = []
        self.line_content_text_list = []
        self.line_type_button_list = []
        self.line_label_button_list = []

        for line_index, line in enumerate(file_content):
            line_index_label = Label(self, width=15, height=5, text=str(line_index))
            line_index_label.grid(row=line_index, column=0, sticky=W + E + N + S)
            line_content_text = Text(self, width=15, height=5)
            line_content_text.insert(INSERT, line)
            line_content_text.grid(row=line_index, column=1, sticky=W + E + N + S)
            line_type_button = Button(self, text="Type", width=25)
            line_type_button.grid(row=line_index, column=2, sticky=W + E + N + S)
            line_label_button = Button(self, text='Label', width=25)
            line_label_button.grid(row=line_index, column=3, sticky=W + E + N + S)

        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)


def command_line_annotate(training_data_dir_path, index, file_path, file_content):
    with open(os.path.join(training_data_dir_path, str(index) + '.txt'), 'wt', encoding='utf8') as f:
        for line_index, line in enumerate(file_content):
            print('Line #' + str(line_index) + ': ', line)
            data_type = input('Type for line #' + str(line_index) + ' (options: 0=header 1=meta 2=content):')
            label = input('Label for line #' + str(line_index) +
                          ' (options: 0=experience 1=knowledge 2=project 3=others')
            f.write(data_type + '\t' + label + '\t' + line)
            f.write('\n')


def gui_annotate(training_data_dir_path, index, file_path, file_content):
    print('run this!!!')
    AnnotatorGui(file_content).mainloop()
    with open(os.path.join(training_data_dir_path, str(index) + '.txt'), 'wt', encoding='utf8') as f:
        pass


def main():
    data_dir_path = './data'  # directory to scan for any pdf files
    training_data_dir_path = './data/training_data'
    collected = read_pdf_and_docx(data_dir_path, command_logging=True, callback=lambda index, file_path, file_content: {
        gui_annotate(training_data_dir_path, index, file_path, file_content)
    })

    print('count: ', len(collected))


if __name__ == '__main__':
    main()
