# searchspider.py
# CSCI151

import pathlib
import sys
import stdio
import os

search = sys.argv[1]
if len(sys.argv) == 3:
    path = sys.argv[2]
else:
    path = os.getcwd()

stdio.writeln("Searching for " + search)

file_list = []


def recursive_search(dirpath):
    p_path = pathlib.Path(dirpath)
    dirs = [directory for directory in p_path.iterdir() if directory.is_dir()]
    files = [file for file in p_path.iterdir() if file.is_file()]
    # find files that contain search string within their name
    # then append to list as an absolute path
    for file in files:
        if search in file.name:
            if type(dirpath) != str:
                file_list.append(path + "\\" + dirpath.name + "\\" + file.name)
            else:
                file_list.append(dirpath + "\\" + file.name)
    for directory in dirs:
        # Search deeper directories
        recursive_search(dirpath / directory)


# Reformat path into a singular type for function uniformity
# while having two different kinds of data being passed into the function
# isn't normally an issue for Python, uniform typing is important in other
# languages such as Java and C++
path_reformatted = pathlib.Path(path)

recursive_search(path_reformatted)

stdio.writeln("Found:")
for i in file_list:
    stdio.writeln(i)