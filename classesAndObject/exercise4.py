from swampy.World import World

""" 
world = World()
canvas = world.ca(width=500, height=500, background='white')
bbox = [[-150,-100],[150,100]]
canvas.rectangle(bbox, outline='black', width=2, fill='green4')
canvas.circle([-25,0], 70, outline=None, fill='red')
world.mainloop()
 """

class Point(object):
    """attributes are x and y coordinates"""

def print_point(point):
    print('%g, %g' %(point.x,point.y))

class Rectangle(object):
    """ attributes are left bottom corner Point, right top corner Point
    and color."""

box = Rectangle()
box.corner = Point()
box.corner.lx = -150.0
box.corner.ly = -100.0 
box.corner.rx =  150.0
box.corner.ry =  100.0
box.color = 'red'

world = World()
canvas = world.ca(width=500, height=500, background='white')

def draw_rectangle(canv, rect):
    co_ordinates = [[rect.corner.lx, rect.corner.ly],[rect.corner.rx , rect.corner.ry]]
    canv.rectangle(co_ordinates,fill=rect.color)
#draw_rectangle(canvas, box)
#world.mainloop()


origin = Point()
origin.x = 0.0
origin.y = 0.0
def draw_point(canv, point):
    canv.circle([point.x,point.y],3, fill='black')
#draw_point(canvas,origin)
#world.mainloop()

class Circle(object):
    """attributes are center point list, radius
    and color"""
my_circle = Circle()
center_point = Point()
center_point.x = 0.0
center_point.y = 0.0
my_circle.center = [center_point.x, center_point.y]
my_circle.radius = 70.0
my_circle.color = 'green'

def draw_circle(canv, cir):
    canv.circle(cir.center, cir.radius, outline=None, fill = cir.color)

#draw_circle(canvas, my_circle)
#world.mainloop()

def draw_czech_flag(canv):
    rect = Rectangle()
    rect.corner = Point()
    rect.corner.lx = -150.0
    rect.corner.ly = -100.0
    rect.corner.rx = 150.0
    rect.corner.ry = 100.0
    rect.color = 'white'
    
    joint_x = (rect.corner.rx - rect.corner.lx)/2.5
    joint_y = (rect.corner.ry - rect.corner.ly)/2
    print(joint_y)
    jointPoint = Point()
    jointPoint.x = rect.corner.lx + joint_x     
    jointPoint.y = rect.corner.ly + joint_y 
    
    polygon1 = [[rect.corner.lx,rect.corner.ly],[rect.corner.lx, rect.corner.ry],[jointPoint.x, jointPoint.y]]
    polygon2 = [[rect.corner.lx,rect.corner.ly],[rect.corner.rx, rect.corner.ly],[rect.corner.rx, jointPoint.y],[jointPoint.x, jointPoint.y]]
    draw_rectangle(canv,rect)
    canv.polygon(polygon1,fill='blue')
    canv.polygon(polygon2,fill='red')
draw_czech_flag(canvas)
world.mainloop()





