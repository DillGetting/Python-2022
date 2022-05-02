import os
import sys
import stdio
import pathlib

file = os.listdir(sys.argv[1])


def searchbot(file):
    mycwd = os.getcwd()
    if os.path.isfile(os.getcwd()):
        mydir = os.scandir(mycwd)  # example used and shows the objects
        print(mydir)
        print("afile")
    else:
        print("not a file")
        return file
    if os.path.isdir(os.getcwd()):
        myfiles = os.listdir(mycwd)
        print("directory")
    else:
        print("not found")



    #     if os.path.isdir(os.getcwd()):
    #         print("a dir")
    #     else:
    #         print("not a dir")
    # for f in myfiles:
    #     print(f)
    # for f in mydire:
    #     print(f.name)
    #     print(f.path)


searchbot(file)
