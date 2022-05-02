# Dillon Wilcox and the searchspider still #s

import sys
import stdio
import pathlib
import os

home_path = pathlib.Path.cwd()
filename = sys.argv[1]
current_dir = sys.argv[2]


def find_file_recursion(current_dir, filename):  # trying to use path or filename different
    if filename in os.listdir(current_dir):
        os.path.isfile(filename)
        return filename
        # full_path = os.path.join(current_dir, filename)
    if os.path.isdir(filename):
        os.path.isdir(full_path)
        return find_file_recursion(current_dir, filename)
    else:
        return
