import stdio
import sys
import stdarray


# def Q2(n):
#    n = 6
#    if (n <= 0):
#       return 1
#    return 1 + Q2(n-2) + Q2(n-3)
# print(Q2)


'''a recursive solution that take a command line argument n
and counts down from n
what is the base case
'''
# n = int(sys.argv[1])

# def countdown(n):
#    if n == 0:               # base case
#       print("GO!")
#    else:
#       print(n)
#       countdown(n-1)        # recursive reduction
#
# countdown(int(sys.argv[1]))


# def Q3(n):
#    if (n <= 0):
#       return
#    stdio.writeln(n)
#    Q3(n-2)
#    Q3(n-3)
#    stdio.writeln(n)
# Q3(6)
# the 10th digit was none or 6

# def Q4(n):
#    if (n <= 0):
#       return
#    stdio.writeln(n)
#    Q4(n-2)
#    Q4(n-3)
#    stdio.writeln(n)
# Q4(7)

# def Q5(n):
#    b = stdarray.create1D(n+1, 0)
#    b[0] = 1
#    for i in range(2, n+1):
#       b[i] = 0
#       for j in range(i):
#          b[i] += b[j]
#    return b[n]
#    print(n)
# Q5(8)

def tower(n, left):
   if (n == 0):
      return ' '
   move = ''
   if (left):
      move = str(n) + 'L'
   else:
      move = str(n) + 'R'
   return tower(n, left) + move + tower(n-1, not left)

def main():
   n = int(sys.argv[1])
   stdio.writeln(tower(n, False))

if __name__ == '__main__':
   main()