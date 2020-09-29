"""Write an init method for the Point class that takes x and y as optional 
parameters and assigns them to the corresponding attributes."""

class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y =y

    def print_point(self):
        print('%g, %g'%(self.x, self.y))

origin = Point()
end = Point(3,5)
origin.print_point()
end.print_point()

