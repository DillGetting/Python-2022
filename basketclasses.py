# Dillon Wilcox basketclasses.py Data structure and tester for my basketballRAW.csv file #
# This was used after the data had been pruned and separated. #
# Data was separated with a slightly modified split.py program from the book #

import sys
import stdio
import stddraw
import csv
import stdarray


class BasketBall:
    """
    the structure for the file after it is stripped to 4 columns using
    """

    def __init__(self, Rk, Team, G, MP):
        self.Rk = Rk
        self.Team = Team
        self.G = G
        self.MP = MP

    def end(self): # gets the init attributes but returns just the end
        end = "{:15} {:>20}\n".format("Minutes Played", self.MP)
        return end

    def br(self): # gives the teams rank in a short way if called
        br = "{:<15} {:>20}\n".format("Rank", self.Rk)
        # br += "-" * 75
        return br

    def show(self): # shows the first 4 columns of the file of 4 columns
        # self.show += "{:<15} {:>20}\n".format("Rank", self.Rk)
        show = self.br()
        show += "{:<15} {:>20}\n".format("Team name", self.Team)
        show += "{:<15} {:>20}\n".format("Games", self.G)
        show += "{:<15} {:>20}\n".format("Minutes played", self.MP)
        show += "-" * 78
        show += "\n"
        return show

    def __str__(self): # this was an attempt at private variables and weird functions
        result = str(self.Team) + ' Games played and rank ('
        result += str(self.G) + ', ' + str(self.Rk) + ')'
        return result # nothing to do with the assignment really.


def tester(): # testing this file with practice data manually in this tester
    Rk = "2"
    Team = "Memphis Grizzlies"
    G = "79"
    MP = "19060"
    ball = BasketBall(Rk, Team, G, MP)
    assert(ball.Rk == Rk)
    assert(ball.Team == Team)
    assert(ball.G == G)
    assert(ball.MP == MP)
    print("good")


if __name__ == "__main__":
    tester()