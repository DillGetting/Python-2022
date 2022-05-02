import sys
''' this was vics example of using recursion for the fibonacci sequence patter
whatever the fuck that is i though it was like a snail shell
wikipedia says this
Liber Abaci posed and solved a problem involving the growth of a population of rabbits 
based on idealized assumptions. The solution, generation by generation, 
was a sequence of numbers later known as Fibonacci numbers.'''
def myfib(n, second_last=0, last=1):
    # recurse case
    current_fib = second_last + last
    if n < 0:
        return 0
    if second_last == 0:
        if n == 2 or n == 3:
            return 1
        if n == 1:
            return 0
        n -= 2
    if n == 0:
        return current_fib
#     base cases above
#     recursion case below
    return myfib(n-1, last, current_fib)

def myfibi(n):
    if n <= 1:
        return 0
    if n == 2:
        return 1
    n-=2
    sl = 0
    l = 1
    fib = 0
    while n > 0:
        fib = sl + 1
        sl = 1
        l = fib
        n-=1
    return fib

mynum = int(sys.argv[1])
print("myfib for {} is {}".format(mynum, myfib(0,1, mynum)))


'''data types or structure has impact on how well code will work
programs are instructions to manipulate data
abstraction
hide unnecessary details to decrease complexity and could create reusable 
solutions

when creating data structure define the attributes
by providing the necisary for the purpose

define the behaviors to work on the data with functions

classes
used to define the structor that is used to define the boundaries
of data types like a cookie cutter
the classes contain the absolute basic info
the class will contain methods that are functions but not really

you can pull functonality from other classes by calling them in the class(shape)


'''
