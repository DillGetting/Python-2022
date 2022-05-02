import stdio
import sys

n = int(sys.argv[1])

# global code if needed

# base case is the stating point in design
product = 1  # my guess at the base case

# and recursive step is the next after base case
# and once the function or whatever is specified in terms of itself like a fractal in nature.
# the infinite repetition of the same result but in respect to itself and therefore
# a pattern can be represented that repeats into itself or out.
# gives a way to simulate similar patterns in math except with any object in python
# once you hit the base case you are done

for i in range(1, n + 1): # must add one due to python starting indexing at 0
    product *= i          # so without you would get the factorial of the number 3 instead of 4

stdio.writeln(product)
# this is the recursive step in line 22 in how it uses the loops results in the final print
# once given the input or if it was a variable instead (n) it would loop over itself in a factorial way
# factorial is n! = n * (n-1) * (n-2) and so on...
# like 4! = 4 * 3 * 2 * 1 = 24
# n! or anything like that only stands for the mathematical symbol for factorial in the dumb nerd formula

# can accomplish loops that refer to themselves without using a loop
# resulting in much less code to write due to the repeating nature and the isolation
# of the scope to play well with more code
# if n == 0 is a base case


# instead of looping we need to call the function in the function
# base case and recursion case
# can have more than one base case
