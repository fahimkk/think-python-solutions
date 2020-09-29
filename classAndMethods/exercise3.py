"""Write a str method for the Point class. Create a Point object and print it."""

class Point(object):
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return '%g, %g'%(self.x, self.y)

point1=Point(4,8)
print(point1)
