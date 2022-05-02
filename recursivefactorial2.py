import stdio
import sys

def main():
    N = int(sys.argv[1])

    total = 1
    term = N # starts at N and reduces to 1
    while(term >= 1):
        total = total * term
        term = term -1
    stdio.writeln(total)

if __name__ == '__main__':
    main()

# another example of factorial below in a different way

def factorial(n):
    if n == 1:
        return n * factorial(n-1)

stdio.writeln(factorial(int(sys.argv[1])))