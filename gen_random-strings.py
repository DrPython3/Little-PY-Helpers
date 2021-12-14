#!/usr/local/opt/python@3.8/bin/python3
# -*- coding: utf-8 -*-

'''
** gen_random-strings **
Generates random strings of any length.

Part of "Little PY-Helpers" @ GitHub.com
'''

__author__ = 'DrPython3'
__date__ = '2021-12-14'
__version__ = '1.0'
__contact__ = 'https://github.com/DrPython3'

# [NEEDED PACKAGES]:
import argparse
import random
import string

# [SETUP ARGS]:
user_args = argparse.ArgumentParser(
    description='Random Strings Generator v1.0 -- DrPython3 @ GitHub.com'
)
user_args.add_argument(
    '-s',
    '--symbols',
    help='Choose symbols to use: (1) lower letters, (2) all letters, (3) alphanumeric.',
    required=True
)
user_args.add_argument(
    '-l',
    '--length',
    help='Length of generated string, e.g. 6',
    required=True
)
get_user_args = user_args.parse_args()

# [VARIABLES]:
user_symbols = int(get_user_args.symbols)
user_length = int(get_user_args.length)

# [GENERATOR]:
if user_symbols == 1:
    available_symbols = string.ascii_lowercase
elif user_symbols == 2:
    available_symbols = string.ascii_letters
elif user_symbols == 3:
    available_symbols = string.ascii_letters + string.digits

generated_string = ''.join(random.choice(available_symbols) for _ in range(user_length))
print(
    '\n\n[RANDOM STRING =] ' + str(generated_string) + '\n\nBye bye!'
)
