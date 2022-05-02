





     def draw(self):
        '''
        This draws the rectangle
        '''
        self._x = x
        self._y = y
        self._width = w
        self._height = h
        stddraw.rectangle(x, y, w, h)


if __name__ == "__main__":
    '''
    This is meant to be the test client running
    the above program.
    '''
    n = int(sys.argv[1])
    lo = float(sys.argv[2])
    hi = float(sys.argv[3])

    n_rects = {}

    stddraw.setXscale(0, 1.5)
    stddraw.setYscale(0, 1.5)

    while n > 0:
        x = random.uniform(lo, hi)
        y = random.uniform(lo, hi)
        w = random.uniform(lo, hi)
        h = random.uniform(lo, hi)
        Rectangle(x, y, w, h)
        for key in n_rects:
            n_rects[key] = Rectangle(x, y, w, h)
        Rectangle.draw(Rectangle)
        n -= 1


    stddraw.show()



# james said this

    # Compiles a list of line segments for draw()
    def _lines(self):
        coords = self.coordinates()
        return [(coords[0], coords[2], coords[0], coords[3]),
                (coords[0], coords[3], coords[1], coords[3]),
                (coords[1], coords[2], coords[1], coords[3]),
                (coords[0], coords[2], coords[1], coords[2])]

    # Draw self on stddraw.
    def draw(self):
        stddraw.setPenRadius(0.002)
        for line in self._lines():
            stddraw.line(line[0], line[1], line[2], line[3])



      for i in range(n):
        # Generates n rectangles within the bounds of lo, hi
        # rounds to 2 decimal places to allow coincident lines
        x = round(random.uniform(lo, hi), 2)
        y = round(random.uniform(lo, hi), 2)
        width = round(random.uniform(lo, hi), 2)
        height = round(random.uniform(lo, hi), 2)
        rectangle = Rectangle(x, y, width, height)
        rectangles.append(rectangle)
        areas.append(rectangle.area())
        perimeters.append(rectangle.perimeter())



    n_rects = {}

    # stddraw.setXscale(0, 1.5)
    # stddraw.setYscale(0, 1.5)

    while n > 0:
        x = stdrandom.uniformFloat(lo, hi)
        y = stdrandom.uniformFloat(lo, hi)
        w = stdrandom.uniformFloat(lo, hi)
        h = stdrandom.uniformFloat(lo, hi)
        # x1 = x + w
        # y1 = y + h
        Rectangle(x, y, w, h)
        for key in n_rects:
            n_rects[key] = Rectangle(x, y, w, h)
            n -= 1
            Rectangle.draw(Rectangle(x, y, w, h))