# -*- coding: utf-8 -*-
# @File:        pdf_merge.py
# @Description:
# @Author:      zuo
# @Time:        2021/12/16 17:29

import os
from PyPDF2 import PdfFileReader, PdfFileWriter


def pdf_merge(input_path, out_path='out.pdf'):
    """
    :param input_path:
    :param out_path:
    """
    root, dirs, files = os.walk(input_path).__next__()
    filenames = [f"{root}/{file}"for file in files if file.split('.')[-1] == 'pdf']
    filenames.sort()

    file_merger = PdfFileWriter()
    for filename in filenames:
        pdf = PdfFileReader(open(filename, "rb"), strict=False)
        for page in range(pdf.getNumPages()):
            file_merger.addPage(pdf.getPage(page))

    with open(out_path, "wb") as output_stream:
        file_merger.write(output_stream)


if __name__ == '__main__':
    pdf_merge(input_path='./data')
