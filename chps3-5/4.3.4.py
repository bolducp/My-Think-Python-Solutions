#my solution with help from Downey

from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()

def polygon(t, length, n):
    t.delay = 0.01
    for i in range(n):
        fd(t, length)
        lt(t, (360/n))

def circle(t, r):
    circum = 2 * r * math.pi
    n = int(circum / 10) + 1
    length = circum / n
    polygon(t, length, n)

circle(bob, 45)