# Dillon Wilcox streams.py
# This is the original filesplitting program used to get a smaller file with the information
# I wanted from the original csv file. #

import instream
import outstream
import sys
import stdio
import stdarray
from instream import InStream
from outstream import OutStream

# infile = instream.InStream(sys.argv[1])
# outfile = outstream.OutStream(sys.argv[2])
#
# mylines = []
#
# while infile.hasNextLine():
#     mylines.append(infile.readLine())
#
# for l in mylines:
#     outfile.writeln(l)

####### The above code takes the file name you give it and creates a new file of the 2nd argument ##

def filespliter():
    delim = ','

    filename = sys.argv[1]
    outfile = int(sys.argv[2])

    inStream = InStream(filename + '.csv')

    outStreams = stdarray.create1D(outfile)
    for i in range(outfile):
        file = OutStream(filename + str(i) + '.csv')
        outStreams[i] = file

    while inStream.hasNextLine():
        line = inStream.readLine()
        fields = line.split(delim)
        for i in range(outfile):
            outStreams[i].writeln(fields[i])


# filespliter()
#### the above code was supposed to separate my original csv file. ########
#### The first 4 columns were stripped from the csv file to be used in the drawing #####

