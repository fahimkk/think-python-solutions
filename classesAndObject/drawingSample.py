from swampy.TurtleWorld import *
from swampy.World import World

tutworld = TurtleWorld()
bob = Turtle()
for i in range(4):
    fd(bob, 100)
    lt(bob)

wait_for_user()
#-------------
world = World()
canvas = world.ca(width=500, height=500, background='white')

bbox = [[-150,-100],[150,100]]
canvas.rectangle(bbox, outline='black', width=2, fill='green4')

canvas.circle([-25,0], 70, outline=None, fill='red')

points=[[-150,-100],[150,100],[150,-100]]
canvas.polygon(points, fill='blue')

world.mainloop()