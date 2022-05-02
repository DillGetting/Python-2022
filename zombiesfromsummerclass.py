import random
import array

R = .1 # immunity rate


def infect(a, x, y):
    d = 1  # distance from x, y
    a[x][y] = 'Z'  # infect Patient Zero

    outputWorld(a)

    while d <= len(a):
        for i in range(x - d, x + d):
            if i >= 0 and i < len(a):  # don't go out of array bounds
                for j in range(y - d, y + d):
                    if j >= 0 and j < len(a):  # don't go out of bounds
                        if a[i][j] != 'i':
                            a[i][j] = 'Z'  # does not check for immunity, just turns everyone into zombies

        print(d)
        outputWorld(a)
        d = d + 1


def outputWorld(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end='.')
        print()
    print()


def createWorld(x, y):
    rows, cols = (10, 10)
    arr = []
    for i in range(cols):
        col = []
        for j in range(rows):
            col.append('.')
        arr.append(col)
    return arr


def immune(R):
    I = random.randint(1, 100)
    print(I)
    if I < R * 100:
        return True
    else:
        return False


def immunify(a):
    for i in range(len(a)):

        for j in range(len(a[i])):
            if immune(R):
                a[i][j] = 'i'


def main():
    pass


if __name__ == '__main__':
    main()


    class World:
        def __init__(self, PersonN, PersonZ, PersonIm):
            self.PersonNormal = PersonN
            self.PersonZomby = PersonZ
            self.PersonImmune = PersonIm

        # def PersonN(self):