# Dillon Wilcox searchspider #

# The programs example results are at the bottom for a successful search with the file found
# I will include what happens when the file (sys.argv[1]) is not found under the successful run

import os
import pathlib
import sys
from pathlib import Path

print("searching for: " + (sys.argv[1]))


def search(n):
    p = pathlib.Path()
    file = [f for f in p.iterdir() if f.is_file()]
    path = [d for d in p.iterdir() if d.is_dir()]
    for f in file:
        if os.path.isfile(filename):
            return filename
    for d in path:
        if os.path.isdir(sys.argv[1]):
            return path
    return search(filename / pathlib.PureWindowsPath())


filename = sys.argv[1]
pathlib.PureWindowsPath = sys.argv[2]

print(search(sys.argv[1]))

# PS C:\Users\diljl\py> python Final_searchspider.py test.txt C:\Users\diljl\py
# searching for: test.txt
# test.txt
# PS C:\Users\diljl\py>


# The program will give the filename back to you after running it if the filename exists

# If there is no file found with the given name I get an error like this

# PS C:\Users\diljl\py> python Final_searchspider.py test C:\Users\diljl\py
# searching for: test
# Traceback (most recent call last):
#   File "C:\Users\diljl\py\Final_searchspider.py", line 30, in <module>
#     print(search(sys.argv[1]))
#   File "C:\Users\diljl\py\Final_searchspider.py", line 24, in search
#     return search(filename / pathlib.PureWindowsPath())
# TypeError: 'str' object is not callable
