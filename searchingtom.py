import pathlib
import sys
import stdio


def spider(path, search):
    """
    This function looks through the chosen path
    for the chosen string. It is meant to work
    recursively to do so.
    """
    # setting the working directory from the parameter
    # provided and creating lists out of directories
    # and files found.
    p = pathlib.Path(path)
    dirs = [d for d in p.iterdir() if d.is_dir()]
    files = [f for f in p.iterdir() if f.is_file()]

    # searching the chosen directory
    for file in files:
        if search in file.name:
            stdio.writeln(file)

    # searching subdirectories
    for dir in dirs:
        spider(dir, search)


# Taking command-line arguments as input for the
# search string as well as the path to start from,
# defaulting to the current working directory as
# well as searching for '.exe' if no arguments are
# entered.

cwd = pathlib.Path.cwd()
search = sys.argv[1] if len(sys.argv) >= 2 else '.exe'
path = sys.argv[2] if len(sys.argv) >= 3 else cwd

# This is to run and format the data per the
# expectations of the assignment.

stdio.writeln()
stdio.writeln('Searching for: ' + search)
stdio.writeln()
stdio.writeln('Found: ')
stdio.writeln()
stdio.writeln(spider(path, search))