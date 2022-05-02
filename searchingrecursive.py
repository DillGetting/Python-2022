import os
import pathlib
import sys
import stdio

file = (sys.argv[1])
path = os.listdir(sys.argv[2])


def search(file, path):
    for element in path:
        if os.path.join(path, file) == os.path.join(file, path):
            return os.path.join(path, file)

    if os.path.isdir(os.path.join(file, path)):
        return os.path.join(file, path), file
    if path is not None:
        return path


search(file, path)