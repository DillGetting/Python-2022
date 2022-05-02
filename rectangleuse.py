# Dillon Wilcox
# Assignment 12 Client
# Rectangleuse.py
# 3.2.1. 3.2.2 and 3.2.3 in the textbook




from rectangles12 import Rectangle
import stdio
import sys
import stddraw
import rectangles12
import stdrandom

# lo = 20.0
# hi = 15.0
#
# x = stdrandom.uniformFloat(lo, hi)
# y = stdrandom.uniformFloat(lo, hi)
x = 20.0
y = 20.0
w = 15.0
h = 10.0


test = Rectangle(x, y, w, h)
print(test.perimeter())
print(test.area())
test.draw()


