
import stdio
import random

# ll two six-sided dice, and write the resulting sum to standard
# output.

SIDES = 6

a = random.randrange(1, SIDES+1)
b = random.randrange(1, SIDES+1)

total = a + b

stdio.writeln(total)