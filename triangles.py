import sys
import stddraw
import math
import stdio


def filledtriangle(x, y, s):
    stddraw.setPenColor(stddraw.BLUE)
    stddraw.filledPolygon(x, y)


def midpoints(x, y):
    xmpb = (x[0] + x[1]) / 2
    ympb = (y[0] + y[1]) / 2

    xmpl = (x[0] + x[2]) / 2
    ympl = (y[0] + y[2]) / 2

    xmpr = (x[1] + x[2]) / 2
    ympr = (y[1] + y[2]) / 2


def sierpinski(n, x, y, s):
    n = int(sys.argv[1])
    x = [0, 1, 5]
    y = [0, 0, math.sqrt(3) / 2]
    if n > 0:
        xmpb = (x[0] + x[1]) / 2
        ympb = (y[0] + y[1]) / 2
        xmpl = (x[0] + x[2]) / 2
        xmpr = (x[1] + x[2]) / 2
        ympr = (y[2] + y[2]) / 2
        ympl = (y[0] + y[2]) / 2

        x = [xmpb, xmpl, xmpr]
        y = [ympb, ympl, ympr]

    filledtriangle(x, y, s)
    n = int(n) - 1
    return


if __name__ == "__main__":
    n = sys.argv[1]
    x = [0, 1, 5]
    y = [0, 0, math.sqrt(3) / 2]
    stddraw.setPenColor(stddraw.GRAY)
    stddraw.polygon(x, y)
    s = 1
    sierpinski(n, x, y, s)
    stddraw.show()
