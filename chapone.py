import stdio
import sys
import stddraw
import stdarray
import random

n = int(sys.argv[1])

a = stdarray.create2D(n, n, 0)

for i in range(n):
    for j in range(n):
        a[i][j] = n * j + i

stdio.writeln("Before")
stdio.writeln("----")
for row in a:
    for element in row:
        stdio.writeln('%4d' % element)
    stdio.writeln()

for i in range(n):
    for j in range(i + 1, n):
        temp = a[i][j]
        a[i][j] = a[j][i]
        a[j][i] = temp

stdio.writeln()
stdio.writeln("After")
stdio.writeln("----")
for row in a:
    for element in row:
        stdio.write('4%d' % element)
    stdio.write()
