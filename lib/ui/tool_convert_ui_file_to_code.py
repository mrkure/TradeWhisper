# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 11:06:41 2020

@author: 42073
"""
import os, sys
# sys.path.append(r'..\lib')
# import functions_io as fio


current_dir = os.path.dirname(os.path.realpath(__file__))

from os import walk

files = []
for (dirpath, dirnames, filenames) in walk(current_dir):
    break
for file in filenames:
    if '.ui' in file:
        files.append(file)
        
if files:
    for file in files:
        # input_file = fio.get_part_of_path(file, -1)
        output_file = file.split('.')[0]+'.py'

        result = r'pyuic5 -x {}\{} -o {}\{}'.format(current_dir, file, current_dir, output_file)
        os.system(result)