# os.path.isdir()
# and os.path.isfile()
# the file is the base case
# the directory is the recursive part.
# check for the file name in each directory
# down to where you can get to the base case of
# variable == os.path.isfile()
import sys
from pathlib import Path
from typing import List

import stdio
import pathlib
import os

# Take in 2 command line arguments

# BASE CASES
# The string that you want to search for: os.path.isfile()
# The directory that you want to search in: os.path.isdir()

# recursive step
# if file_to_search_for is not found in search_start directory return
# if file_to_search_for is found in the search_start directory os.path.isfile()

cwd = pathlib.Path.cwd()

file_to_search_for = sys.argv[1]

path_to_search = sys.argv[2]


def search_recursive(searcher):
    path = pathlib.Path(path_to_search)
    # starting with the given input to search over each directory and file in that path
    # for the file_to_search_for

    directories = [directory for directory in path.iterdir() if directory.is_dir()]
    file = file_to_search_for
    for files in file:
        if os.path.isdir(path_to_search):
            return file
    print(file_to_search_for)
    for directory in directories:
        if file_to_search_for in path_to_search:
            return directories
        return search_recursive(path_to_search / directory)
    print(search_recursive(path_to_search))


search_recursive('test.txt')
