# Dillon Wilcox sports assignment part 2
# basketfilter.py
# The filesplitter function takes in my csv file after and splits it into however many
# columns that you ask it to. I chose 4.

# The program does take an argument of a csv file.
# But it will only graph the specific csv file data that I have
# That is the best I could do I will include the file.

# I had to pip install matplotlib to let the program work right.

import csv
import stddraw
import basketclasses
import instream
import outstream
import sys
import stdio
import stdarray
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from instream import InStream
from outstream import OutStream


def main():
    """
    Taking in the file and reading it into a list data structure
    using the functions created in classes in the basketclasses.py file.
    I did not try this on any other data but the file i provided as it is
    tailored for that data.
    """
    basketcsv = sys.argv[1] # the file you supply
    ballerlist = [] # empty list space for use later
    with open(basketcsv, encoding="UTF_8") as fd: # read the given csv file from the command line
        reader = csv.DictReader(fd) # read the file out
        for row in reader: # iterate and list the rows I wanted for something important, research
            ballerlist.append(basketclasses.BasketBall(row["Rk"], row["Team"], row["G"], row["MP"]))
        for b in ballerlist: # the empty list ballerlist was filled
            print(b.show()) # I just wanted to list it out based on the class from another module
            print(b.__str__()) # I know this is illegal I was just experimenting
    rank = [] # empty list for the ranks
    minutes_played = [] # empty list for the minutes played

    with open(basketcsv, 'r') as csvfile: # open the csv file in read mode using different method
        lines = csv.reader(csvfile, delimiter=',') # establish the different items in the lists
        for row in lines:
            rank.append(row[0]) # go through all the first values in the file before a ',' and add to the rank list
            minutes_played.append(row[3]) # go through all the 4th values in the file to add to the Minutes_played list
    plt.scatter(rank, minutes_played, color = 'g',s = 100) # the type of graph with format and boundaries
    plt.xticks(rotation = 25) # the points on the graph style and size
    plt.xlabel('Rank') # taken from the file for x axis
    plt.ylabel('Minutes_played') # the y axis taken from the named column of the file being used
    plt.title('Team rank compared to minutes played', fontsize = 20) # title for the graph

    plt.show() # calls the matplotlib to draw the graph. way better looking then the booksite stddraw

# Unsure how to add this code below. It is the code that separated my original huge csv into
# 4 smaller output files that were combined

# def filesplitter():
#     delim = ','
#
#     # filename = sys.argv[1]
#     # outfile = int(sys.argv[2])
#
#     inStream = InStream(filename + '.csv')
#
#     outStreams = stdarray.create1D(outfile)
#     for i in range(outfile):
#         file = OutStream(filename + str(i) + '.csv')
#         outStreams[i] = file
#
#     while inStream.hasNextLine():
#         line = inStream.readLine()
#         fields = line.split(delim)
#         for i in range(outfile):
#             outStreams[i].writeln(fields[i])
# filesplitter()

#### the above code was supposed to separate my original csv file. ########
#### The first 4 columns were stripped from the csv file to be used in the drawing #####


if __name__ == "__main__":
    main()

# The output for the file looks like this but for every team in the file.
# The plot is in the word document if you don't want to download matplotlib

# PS C:\Users\diljl\py> python basketfilter.py basketballRAW.csv
# pygame 2.1.2 (SDL 2.0.18, Python 3.9.10)
# Hello from the pygame community. https://www.pygame.org/contribute.html
# Rank                               1
# Team name       Minnesota Timberwolves
# Games                             80
# Minutes played                 19300
# ------------------------------------------------------------------------------


