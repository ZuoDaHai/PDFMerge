# -*- coding: utf-8 -*-
# @File:        pdf_merge.py
# @Description:
# @Author:      zuo
# @Time:        2021/12/16 17:29

import os
from PyPDF2 import PdfFileReader, PdfFileWriter


def read_file(filenames):
    for filename in filenames:
        yield PdfFileReader(open(filename, "rb"), strict=False)


def pdf_merge(input_path, out_path='out.pdf'):
    """
    :param input_path:
    :param out_path:
    """
    root, dirs, files = os.walk(input_path).__next__()
    filenames = [f"{root}/{file}"for file in files if file.split('.')[-1] == 'pdf']
    filenames.sort()

    file_merger = PdfFileWriter()
    for pdf in read_file(filenames):
        for page in range(pdf.getNumPages()):
            file_merger.addPage(pdf.getPage(page))

    output_stream = open(out_path, "wb")
    file_merger.write(output_stream)
    output_stream.close()


if __name__ == '__main__':
    pdf_merge(input_path='./data')
