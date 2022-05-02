# Dillon Wilcox and the Searchspider.py #

import sys
import stdio
import pathlib
import os
from pathlib import Path
from glob import glob, iglob


# search spider will look through all the files in a given directory
# find the file name given from the command line inputs of 2 arguments
# search-string or the file you want to search for in normal words is the first arg
# the path of the folder you are searching or the starting path for you spider slave


# It does not work to search a directory. It just spits it back at you
def dirsearch(dirpath):
    p = pathlib.Path(dirpath)
    dirs = [d for d in p.iterdir() if d.is_dir()]
    files = [f for f in p.iterdir() if f.is_file()]
    for f in files:
        if os.path.isdir(p):
            return p
    for d in dirs:
        if d in dirpath:
            print('Found it ')
        return dirsearch(dirpath / dirs)


def main():
    # cwd = pathlib.Path.cwd()
    search = sys.argv[1]
    path = sys.argv[2] if len(sys.argv) >= 3 else cwd
    stdio.writeln("Searching for ")
    stdio.writeln(search)
    print('Found it ')


if __name__ == "__main__":
    main()

# PS C:\Users\diljl\py> python searchspider.py test.txt C:\\Users\diljl\py
# Searching for
# test.txt
# Found it


# My second try at the problem I have below
""" This is my Final answer as the best I could come up with if it comes to that
They all do a part of the problem though."""


f = sys.argv[1]  # global code that takes the input given
dpath = sys.argv[2]  # should this be in a def main() followed by
print("searching for: ", f)  # if __name__ == "__main__": main()?


def bot(f, dpath):  # takes in the file you want to search for and directory you are starting at
    """ if os.path.isfile(f) returns true if f is a file in the directory
    else, or if not, it prints not found and returns to scan for if f is a directory,
    checks if dpath (returns true or false) is the path the file f is in,
    else print not a directory.

    That was the plan at least"""

    if os.path.isfile(f):  # base case
        print("file", f, "found")
    else:
        print("not found")
        return os.scandir(bot(f, dpath))  # attempted reduction or recursive step
    if os.path.isdir(dpath):  # base case
        print("is in :", dpath)  # print the path given to confirm given path is where the file is
    else:
        print("not a directory either")  # prints if the given path dpath is not a valid path for the file
    myfiles = os.listdir(dpath)  # trying a different tactic as you showed us: lists files in dpath
    mydir = os.scandir(dpath)  # scans for DirEntry objects
    for x in myfiles:  # preparing to iterate over the listed files from os.listdir(dpath)
        if os.path.isfile(f):  # if the listed files in f are files: base case
            return f
        print(f)# return the file
    for y in mydir:  # looking over the DirEntry objects: base case
        if os.path.isdir(dpath):  # if and of the DirEntry objects found are in the given dpath
            return bot(y, dpath)  # recursive step here but so far cannot figure that out


bot(f, dpath)  # call to the function to run the code


# Output of both of these programs when the file is found #

# Both of the functions here will search for a file in the current working directory
# not in any directory, but it still wants an accurate path
# for the second command line argument.

# I think I was not able to figure out a proper recursive step.


# PS C:\Users\diljl\py> python searchspider.py test.txt C:\Users\diljl\py
# Searching for
# test.txt
# Found it
# searching for:  test.txt
# file test.txt found
# is in : C:\Users\diljl\py


# Here is the third try to this problem #
"""This function also just lists all the objects and DirEntries in the given path.
So I commented it out."""

# def search():
#     myfiles = os.listdir()
#     for f in myfiles:
#         if os.path.isfile(f):  # here is where the base cases are
#             print("its a file", os.path.abspath(f))
#         if os.path.isdir(f):  # base case
#             print("its a dir", os.path.abspath(f))
#         return f
#
#
# search()


# I thought I was on to something but could not get further that this.

# Output of the search function

# PS C:\Users\diljl\py> python files.py test.txt C:\Users\diljl\py
# its a dir C:\Users\diljl\py\.idea


# Fourth attempt below #


# def spidery():
#     myfiles = os.scandir()
#     for i in myfiles:
#         if os.DirEntry.is_file(i):
#             print("its a file")
#         if os.DirEntry.is_dir(i):
#             print("its a dir")
#     myfiles = os.listdir()
#     for i in myfiles:
#         if os.path.isfile(i):  # here is where the base cases are
#             print("its a file", os.path.abspath(f))
#         if os.path.isdir(i):  # base case
#             print("its a dir")
#
#
# spidery()

# PS C:\Users\diljl\py> python searchspider.py test.txt C:\Users\diljl\py
# Searching for
# test.txt
# Found it
# searching for:  test.txt
# file test.txt found
# is in : C:\Users\diljl\py
# its a dir C:\Users\diljl\py\.idea
# its a dir
# its a file
# its a file
# its a file
# ... ect


# I commented out the spidery() function due to how much it prints out.
# The example output is on line 148 #
