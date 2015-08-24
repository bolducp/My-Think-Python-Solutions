from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()

def koch_curve(t, length):
    t.delay = 0.01
    if length < 3:
        fd(t, length)
        return
    koch_curve(t, (length/3.0))
    lt(t, 60)
    koch_curve(t, (length/3.0))
    rt(t, 120)
    koch_curve(t, (length/3.0))
    lt(t, 60)
    koch_curve(t, (length/3.0))

koch_curve(bob, 200)

wait_for_user()