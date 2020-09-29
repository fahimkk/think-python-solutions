"""Write a function named move_rectangle that takes a Rectangle and two numbers 
named dx and dy. It should change the location of the rectangle by adding dx to 
the x coordinate of corner and adding dy to the y coordinate of corner"""

class Point(object):
    """attributes are x and y coordinates"""

def print_point(point):
    print('%g, %g' %(point.x,point.y))

class Rectangle(object):
    """ attributes are width, height and corner Point"""

box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 4.5
box.corner.y = 3.5

def move_rectangle(rect, dx, dy):
    rect.corner.x += dx
    rect.corner.y += dy

print_point(box.corner)
move_rectangle(box, 2, 4)
print_point(box.corner)