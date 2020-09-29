"""Write an add method for Points that works with either a Point object or a tuple:
If the second operand is a Point, the method should return a new Point whose x coordinate 
is the sum of the x coordinates of the operands, and likewise for the y coordinates.
If the second operand is a tuple, the method should add the first element of the tuple to the x 
coordinate and the second element to the y coordinate, and return a new Point with the result."""


class Point(object):
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return '%g, %g'%(self.x, self.y)
    def __add__(self, other):
        if isinstance(other,Point):
            return self.add_points(other)
        else:
            return Point(self.x+other[0], self.y+other[1])
    def add_points(self,other):
        return Point(self.x+other.x, self.y+other.y)
    def __radd__(self,other):
        return self.__add__(other)

point1=Point(4,8)
point2=Point(6.4,.8)
point3 = point1+point2
point4 = point1 +(3,5)
point5 = (3,5)+point1
print(point3)
print(point4)
print(point5)