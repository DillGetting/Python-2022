'''encapsulation is a term to know
comparing classes to cookie cutter
making a stucture that can be slammed onto the data to give the data structure

protecting data is the purpose of encapsulation

pure functions have no side effects and only changes the data within the function

    example is the math functions specifically factorial with only give one value back without changing anything else

    method is a

classes are used to define data structure
including functionality
classes create objects
each object that is created is not the same object

but each object that is created from blueprints provided by the class with different data used

if a class is a cookie cutter for data each object can be a different flavor of cookie

for class dog
each dog has different data about its breed age color
and even different behaviors or what the data is representing

classes are used to then apply the breed age color attributes to allow you to describe data

classes also let us describe relations to the data,
example is a shape class with basic attributes
    then a child of shape could be circle or square
    both circle and square inherit those attributes with the child class

    that is the concept of polymorphism (gaaaay)

shape can be the parent of many things becuase of how generalized that term is it only defines the basic
requirements that then can be used on any shape to avoid writeing that over and over

class shape:
    def area(self):
        pass
    def name(self):
        return shape

class square(shape):
    def __init__(self, length): in parenthasis contain the self inheritance and what is unique about the circle
        self.side_len = length

    def area(self):
        return self.side_len * self.side_len

self is a convention just dont think about it too much
all you need to know is that self is the reference to the object
a class is not an object, but create classes
    self is a reference to the memmory location of the paraent
    self.side_len side_len is the variable with self being used as the reference pointer to what to do with the variables data

again just dont think about it
   just remember the structure

   '''

# My module for shape data structures

import math

class shape:

    def area(self):
        pass

    def perimeter(self):
        pass

    def fun(self):
        return "We love geometry"

    def name(self):
        return "shape"

class triangle(shape):
    def __init__(self, height, base):
        self.height = height
        self.base = base

    def area(self):
        return (self.height * self.base) / 2

    def perimeter(self):
        return self.base * 3

    def name(self):
        return "triangle"


