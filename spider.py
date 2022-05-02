# Dillon Wilcox and the searchspider #

import sys
import stdio
import pathlib
import os

# search spider will look through all the files in a given directory
# find the file name given from the command line inputs of 2 arguments
# search-string or the file you want to search for in normal words is the first arg
# the path of the folder you are searching or the starting path for you spider slave

print("Searching for " )

cwd = pathlib.Path.cwd()
search = sys.argv[1]
dirpath = sys.argv[2] # if len(sys.argv) >= 3 else cwd
# path = sys.argv[2] if (sys.argv) == str('.exe') else cwd


def dirsearch(dirpath):
    p = pathlib.Path(dirpath)
    d = os.path.join(dirpath, search)
    dirs = [d for d in p.iterdir() if d.is_dir()]
    files = [f for f in p.iterdir() if f.is_file()]
    for file in files:
        if os.path.isdir(p):
            return p
    for directory in dirs:
        if sys.argv[2] in dirpath:
            return dirpath
        return dirsearch(dirpath / dirs)
dirsearch(dirpath)
    # print(dirpath(d))