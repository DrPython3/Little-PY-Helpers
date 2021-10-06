#!/usr/local/opt/python@3.8/bin/python3
# -*- coding: utf-8 -*-

'''
**rm-duplicates.py**
Remove duplicate lines from textfiles.

Part of "Little PY-Helpers" @ GitHub.com
'''

__author__ = 'DrPython3'
__date__ = '2021-09-19'
__version__ = '1.0'
__contact__ = 'https://github.com/DrPython3'

# [FUNCTION]:

def rm_duplicates(targetfile):
    '''
    Checks each line in a textfile whether its unique or not.

    :param str targetfile: textfile to check
    :return: None
    '''
    already_existing = set()
    lines_checked = 0
    lines_unique = 0
    try:
        with open(targetfile, 'r+') as targetcontent:
            to_check = targetcontent.readlines()
            targetcontent.seek(0)
            for line in to_check:
                lines_checked += 1
                if line.replace('\n', '') not in already_existing:
                    targetcontent.write(line.replace('\n', ''))
                    already_existing.add(line.replace('\n', ''))
                    lines_unique += 1
                else:
                    continue
            targetcontent.truncate()
        del already_existing
        print(f'Lines checked: {str(lines_checked)}')
        print(f'Unique lines left: {str(lines_unique)}')
    except:
        print('Sorry!\nAn error occurred. Check file and try again.')
    return None

# [SAMPLE USAGE]:

testfile = input('Testfile, e.g. testfile.txt: ')
rm_duplicates(str(testfile))
