"""Write a version of move_rectangle that creates and 
returns a new Rectangle instead of modifying the old one."""

import copy

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
    new_rect = copy.deepcopy(rect) 
    new_rect.corner.x += dx
    new_rect.corner.y += dy
    return new_rect

print_point(box.corner)
new_box = move_rectangle(box, 2, 4)
print_point(new_box.corner)
print_point(box.corner)
