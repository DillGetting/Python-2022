"""Do not use a class if there is no Data
    use functions

Everything starts with the data in a class
    the methods are not at important

how to project the data
        you have direct access with self

input setTime() method
output getTime() method

struct in C is like an array of variables, like an object

Immutable: numbers, strings and tuples

Mutable: list, set, Dictionary

        cards should not be mutable for example

The first step to what you do when you have data is use list set or dictionary
        do not need a class if a list set or dictionary can be used instead.
        also called containers

every container is a container of object references and called general containers

API: Application to program interface
    The interface defined in the class
    stdio module is full of interface for the program like readAll()

    The application or client is used in an API request that goes to you data source like a server
    the API responds lastly
    giving the response back to the client in full circle

If there is not enough functionality it is narrow vs wide as the opposite
    example is the book.py title_search

WHEN DESIGNING DATA STRUCTORS or client contract
        write the interface for the data that is needed to be used. (duh?)

MAKE SURE THAT the dependencecy is limited in a hierarchy sort of way
    you have the interface including the application internals and the client can only access
    application through another application of a special user interface


MODULARITY:
    keep like with like
    Example the package game would have sub-packages like sound image and level
    each module is a file like toolkit.
    IMPORT only the file name containing the functions desired. not the class itself


Polymorphism is the ability to treat objects the same: all the objects have a common interface.
    like the class shape can fit many different specific shapes that would use the same properties
    needed for a shape.
Inheritance: also happens


    parking garage in object oriented
        parking space class
        is really all you need.
            is there an open spcace.
                a location.
                    think like a computer game would.
        Object Oriented programming is much more complex then you would think.
            like anything that is worth anything.
        precedural oriented has global data the goes into functions without side effects
            near impossible.
        Best is to use a combination some object orented to the biggest data function behavior with added
        precedural lists (parking garage) to keep it simple.

    OVERLOADING:
        operator overloading is like the + can concatinate strings and add integers.

Shallow vs Deep reference:
    Shallow is when you are referring to the same item or reassigning a reference like a variable.
        list | a = list: a and list are pointing to the same thing. when you reassign they point
        to the same place in memory, or object location.

Always design an API with the user in mind not the other way.





"""