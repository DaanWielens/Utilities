'''
Template for automating a process that converts/analyses file by file.
Using this template, the user selects the folder that contains all files.
The script then recursively goes through these files and runs a script on/with those files.

Usage: python batch-recur.py path/to/folder/with/files
'''
import sys
import os
from glob import glob
from subprocess import call
import shutil

if len(sys.argv) != 2:
    print('Usage: python batch-recur.py path/to/folder/with/files')
    sys.exit()

# Filetype: specify which files should be added to the list:
#   i.e., for .csv files, use: file_type = '*.csv'
file_type = '*.csv'

#Get a list of all files that are in the chosen folder (also the files in the subdirs)
PATH = sys.argv[1]
result = [y for x in os.walk(PATH) for y in glob(os.path.join(x[0], file_type))]
lres = len(result)

for i in range(0,lres):
    file_path = result[i]
    file_dir, file_name = os.path.split(file_path)

    # Change the following line for your own scripts
    call(['some_script','arg1','arg2'])
