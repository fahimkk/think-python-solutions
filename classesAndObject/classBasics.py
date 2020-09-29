import copy

class Point(object):
    """Represents a point in 2-D space"""

blank = Point()
blank.x=3.0
blank.y = 4.0

def print_point(cls):
    print ('%g, %g' %(cls.x,cls.y))

#print_point(blank)

class Rectangle(object):
    """Repressents a rectangle.
    attributes: width, height, corner"""

box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

def find_center(rect):
    """ fuction can return instances ie objects"""
    p = Point()
    p.x = rect.corner.x + rect.width/2.0
    p.y = rect.corner.y + rect.height/2.0
    return p

box_center = find_center(box)
#print(box_center)
#print('---')
#print_point(box_center)

def grow_rectangle(rect, dwidth, dheight):
    """Objects are mutable, we can change the state of an object by 
    making an assignment to one of its arriibutes"""

    rect.width += dwidth
    rect.height += dheight

#print(box.width)
#grow_rectangle(box, 50, 25)
#print(box.width)

p1 = Point ()
p1.x = 3.0
p1.y = 4.0

p2 = copy.copy(p1)
print_point(p1)
print_point(p2)
print(p1 is p2)
print(p1 == p2)
"""you might have expected == to yield True because these points contain the same data. In that case, 
you will be disappointed to learn that for instances, the default behavior of the == operator is the 
same as the is operator; it checks object identity, not object equivalencer"""



