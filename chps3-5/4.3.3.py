from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()

def polygon(t, length, n):
    for i in range(n):
        fd(t, length)
        lt(t, (360/n))

polygon(bob, 120, 5)