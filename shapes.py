# My module for shape data structures

import math

class shape:

    def area(self):
        pass

    def perimeter(self):
        pass

    def fun(self): # this is always going to pass to below unless you overide the function
        return "We love geometry"

    def name(self):
        return "shape"


class square(shape):
    side_len = 0 # is the same as the self.side_len = length

    def __init__(self, length):
        self.side_len = length
# definig an attribute of side_len to square

    def area(self):
        return self.side_len * self.side_len

    def perimeter(self):
        return 4 * self.side_len

    def name(self):
        return "square"

class circle(shape):

    def __init__(self, r):
        self.radius = r

    def area(self): # area is a method can be called with variable.area()
        return math.pi * (self.radius**2)

    def perimeter(self):
        return 2 * math.pi * self.radius

    def name(self):
        return "circle"

# class triangle(shape):
#     def __init__(self, length, width):

