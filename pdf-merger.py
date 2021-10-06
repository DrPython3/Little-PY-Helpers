#!/usr/local/opt/python@3.8/bin/python3
# -*- coding: utf-8 -*-

'''
**pdf-merger.py**
Merges several PDF file into a single one.
Fast and easy to use.

Part of "Little PY-Helpers" @ GitHub.com
'''

__author__ = 'DrPython3'
__date__ = '2021-10-06'
__version__ = '1.0'
__contact__ = 'https://github.com/DrPython3'

# [NEEDED PACKAGES]:

import sys
try:
    import os
    from PyPDF2 import PdfFileMerger
    from PyPDF2 import PdfFileReader
except:
    sys.exit('Sorry, an error occurred while importing needed packages.')

# [FUNCTION]:

def merger(filedir, targetfile):
    '''
    Merges PDF files into a single one within the same directory.
    Encrypted PDF files not supported!

    :param str filedir: directory with several PDF files
    :param str targetfile: name of the new PDF file
    :return: True or False
    '''
    pdf_merger = PdfFileMerger(strict=False)
    target = str('')
    input_pdfs = []
    try:
        pdf_location_valid = os.path.exists(filedir)
        if pdf_location_valid == True:
            os.chdir(filedir)
            pdf_location = os.getcwd()
            if targetfile.find('.pdf') == -1:
                target = targetfile + '.pdf'
            else:
                target = targetfile
            for file in os.listdir(pdf_location):
                if file.endswith('pdf') == False:
                    continue
                else:
                    input_pdfs.append(file)
            for pdf in input_pdfs:
                with open(pdf, 'rb') as file_object:
                    pdf_object = PdfFileReader(file_object, strict=False)
                    pdf_merger.append(pdf_object)
            pdf_merger.write(target)
            pdf_merger.close()
            return True
        else:
            return False
    except:
        sys.exit('Sorry, an error occurred.')

# [SAMPLE USAGE]:

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

print('*** PDF MERGER (c) 2021 DrPython3 ***\n\n'
      + 44*'-' + '\n'
      + 'Merge several PDF files into a single one.\n'
      + 'Note: encrypted PDF files are not supported!\n'
      + 44*'-' + '\n\n')

dir_with_pdfs = str(input('Enter directory with PDF files: '))
single_pdf_name = str(input('Enter name for new PDF file: '))
result = merger(dir_with_pdfs, single_pdf_name)

if result == True:
    print(f'\nDONE!\nSuccessfully merged all PDF files in {dir_with_pdfs} into {single_pdf_name}.')
else:
    print(f'\nSorry!\nCould not merge the PDF files in {dir_with_pdfs}.')
