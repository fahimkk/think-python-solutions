"""Write an add method for the Point class.
the method should return a new Point whose x coordinate is the sum of 
the x coordinates of the operands, and likewise for the y coordinates."""

class Point(object):
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return '%g, %g'%(self.x, self.y)
    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)

point1=Point(4,8)
point2=Point(6.4,.8)
point3 = point1+point2
print(point3)