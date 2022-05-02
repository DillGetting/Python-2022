import stdio
import sys
import stddraw
import stdarray

'''to reverse a string
takes a string arg
returns the string in reverse'''

def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]

def main():
    stdio.writeln(reverse('Bitchin'))

if __name__ == '__main__':
    main()


