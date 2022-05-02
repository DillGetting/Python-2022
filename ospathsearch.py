# Dillon Wilcox recursive searchspider #

import os
import sys

f = sys.argv[1]  # global code that takes the input given
dpath = sys.argv[2]  # should this be in a def main() followed by
print("searching for: ", f)  # if __name__ == "__main__": main()?


def bot(f, dpath):  # takes in the file you want to search for and directory you are starting at
    """ if os.path.isfile(f) returns true if f is a file in the directory
    else or otherwise it prints not found and returns to scan for if f is a directory
    and checks if dpath (returns true or false) is the path the file f is in
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
            return f  # return the file
    for y in mydir:  # looking over the DirEntry objects: base case
        if os.path.isdir(mydir):  # if and of the DirEntry objects found are in the given dpath
            return dpath  # recursive step here but so far cannot figure that out


bot(f, dpath)  # call to the function to run the code
