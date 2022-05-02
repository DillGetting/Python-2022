# Playing with shapes

import shapes

myshapes_list = []
myshapes_list.append(shapes.shape())
myshapes_list.append(shapes.square(5))
myshapes_list.append(shapes.circle(5))

for s in myshapes_list:
    print("I am a {} area: {} perimeter {} hobby: {}".format(s.name(),
          s.area(), s.perimeter(), s.fun()))