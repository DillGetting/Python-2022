# Dillon Wilcox and the searchspider #

import sys
import stdio
import pathlib

from pathlib import Path
import os

# The input and defualt filename are below
current_directory = pathlib.Path.cwd()
search = sys.argv[1]
path = sys.argv[2]


def listdir(rootdir):
    p = pathlib.Path(rootdir)  # the root directory to use
    d = os.path.join(rootdir, search)  # starting place to the search
    if os.path.isdir(path):
        return path  # if the directory is in the path good
    if not os.path.isdir(path):
        return listdir
    return listdir(listdir)  # if not then try other directory was the idea but no


listdir(path)
