import stddraw
import stdio
import sys


def checksum(HaKey):
    '''this is the fundtion that was supposed to cumpute the
    checksum of the zipcode and the result is then run through
    the stddraw module postdrawbar.py to draw the '''
    for i in HaKeyNum:
        HaKey = HaKey + i

    HaKey = HaKey % 10

    return stddraw.text(4.5, 1, str(sys.argv[1]))

