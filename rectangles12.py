# Dillon Wilcox
# Assignment 12 Rectangles module

import stddraw
import stdio
import stdarray
import stdrandom
import sys
import math
import random


class Rectangle:

    # Construct self with center (x, y), width w, and height h.
    def __init__(self, x, y, w, h):
        self._x = x
        self._y = y
        self._width = w
        self._height = h
        self._x1 = self._x + self._width  # for use in draw()
        self._y1 = self._y + self._height  # draw() used to calculate relative coordinates

    # Return the area of self.
    def area(self):
        return self._width * self._height

    # Return the perimeter of self.
    def perimeter(self):
        return (2 * self._height) + (2 * self._width)

    # Return True if self intersects other, and False otherwise.
    def intersect(self, other):
        self._x = max(self._x, other.x)
        self._y = max(self._y, other.y)
        self._x1 = min(self._x1, other.x1)
        self._y1 = min(self._y1, other.y1)
        intersection = max(0, self._x1 - self._x + 1) * max(0, self._y1 - self._y + 1)
        return intersection

    #  returns the min and max coordinate values
    def coordinates(self):
        min_x = self._x - self._height / 2
        max_x = self._x + self._height / 2
        min_y = self._y - self._width / 2
        max_y = self._y + self._width / 2
        return [min_x, max_x, min_y, max_y]

    # Return True if other is completely inside of self, and False
    # otherwise.
    def contains(self, other):
        pass

    # Same as contains() but more strictly contained, does
    # not allow coincident lines
    # def strict_contains(self, other):
    #     rec1_x1, rec1_x2, rec1_y1, rec1_y2 = self.coordinates()
    #     rec2_x1, rec2_x2, rec2_y1, rec2_y2 = other.coordinates()
    #     return rec1_x1 < rec2_x1 <= rec2_x2 < rec1_x2 and \
    #             rec1_y1 < rec2_y1 <= rec2_y2 < rec1_y2

    def _points(self): # this was to attempt to use as a way to get points to draw
        min_x = self._x - self._height / 2
        max_x = self._x1 + self._height / 2
        min_y = self._y - self._width / 2
        max_y = self._y1 + self._width / 2
        return [(min_x, min_y), (min_x, max_y),
                (max_x, min_y), (max_x, max_y)]

    # Draw self on stddraw.
    def draw(self):
        stddraw.setPenRadius(0.1) # I spent a good week trying to figure out why
        # my rectangles were filled, and it turned out the pen was too fat and made them filled...
        stddraw.setXscale(min=0.0, max=70.0)
        stddraw.setYscale(min=0.0, max=70.0)
        stddraw.line(self._x, self._y, self._x1, self._y)  # Draws first line along bottom
        stddraw.line(self._x, self._y, self._x, self._y1)  # second line to the top
        stddraw.line(self._x, self._y1, self._x1, self._y1)  # first line end to new point
        stddraw.line(self._x1, self._y, self._x1, self._y1)  # second line end to new point
        stddraw.show()  # rectangle it


def test():
    n = int(sys.argv[1])  # for the number of rectangles
    lo = float(sys.argv[2])  # for the low float values of options for the rectangles
    hi = float(sys.argv[3])  # the counterpart to the lo variable
    x = stdarray.create1D(n, stdrandom.uniformFloat(lo, hi))  # trying to get an array of values
    y = stdarray.create1D(n, stdrandom.uniformFloat(lo, hi))
    x1 = stdarray.create1D(n, stdrandom.uniformFloat(lo, hi))
    y1 = stdarray.create1D(n, stdrandom.uniformFloat(lo, hi))
    Rectangle(x, y, x1, y1).draw()




    # n_rects = {}
    #
    # # stddraw.setXscale(0, 1.5)
    # # stddraw.setYscale(0, 1.5)
    #
    # while n > 0:
    #     x = stdrandom.uniformFloat(lo, hi)
    #     y = stdrandom.uniformFloat(lo, hi)
    #     w = stdrandom.uniformFloat(lo, hi)
    #     h = stdrandom.uniformFloat(lo, hi)
    #     # x1 = x + w
    #     # y1 = y + h
    #     Rectangle(x, y, w, h)
    #     for key in n_rects:
    #         n_rects[key] = Rectangle(x, y, w, h)
    #         n -= 1
    #         Rectangle.draw(Rectangle(x, y, w, h))
    #



    # for i in range(n):
        # Generates n rectangles within the bounds of lo, hi
        # rounds to 2 decimal places to allow coincident lines
        # x = round(random.uniform(lo, hi), 2)
        # y = round(random.uniform(lo, hi), 2)
        # width = round(random.uniform(lo, hi), 2)
        # height = round(random.uniform(lo, hi), 2)
        # rectangle = Rectangle(x, y, width, height)
        # rectangles.append(rectangle)
        # areas.append(rectangle.area())
        # perimeters.append(rectangle.perimeter())

# FAILED ATTEMPT below. took me a lot of time fiddleing with it though, so I will keep it.
#     x = stdarray.create1D(n, stdrandom.uniformFloat(lo, hi))  # trying to get an array of values
#     y = stdarray.create1D(n, stdrandom.uniformFloat(lo, hi))
#     x.append(stdrandom.uniformFloat(lo, hi))
#     y.append(stdrandom.uniformFloat(lo, hi))  # and the array of the other values needed
#     # for something in range(n):  # go over the something n given times
#     x1 = stdarray.create1D(n, stdrandom.uniformFloat(lo, hi))
#     y1 = stdarray.create1D(n, stdrandom.uniformFloat(lo, hi))
#     x1.append(stdrandom.uniformFloat(lo, hi))
#     y1.append(stdrandom.uniformFloat(lo, hi))


if __name__ == "__main__":
    test()


    # Practice tester:
    # x = "15"
    # y = "20"
    # width = "10"
    # height = "7"
    # test_rectangle = Rectangle(x, y, width, height)
    # assert(test_rectangle._x == x)
    # assert(test_rectangle._y == y)
    # assert(test_rectangle._width == width)
    # assert(test_rectangle._height == height)
    # print("test passed")