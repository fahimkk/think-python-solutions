"""Write a function called distance_between_points that takes 
two Points as arguments and returns the distance between them."""

import math

class Point(object):
    pass

p1 = Point()
p2 = Point()

p1.x,p1.y = (4.0, 0.0)
p2.x,p2.y = (0.0, 3.0)

def distance_between_points(point1,point2):
    return math.sqrt((point2.x-point1.x)**2 + (point2.y-point1.y)**2)

print(distance_between_points(p1,p2))

