"""Modify your solution to Exercise 2 by adding an Entry widget and a second button.
When the user presses the second button, it should read a color name from the Entry
and use it to change the fill color of the circle. Use config to modify the existing
circle; don’t create a new one.
Your program should handle the case where the user tries to change the color of a circle
that hasn’t been created, and the case where the color name is invalid."""

import random

from swampy.Gui import *

g = Gui()
g.title = "Gui"
circle1 = False


def make_circle():
    global circle1
    circle1 = canvas.circle([random.randint(-200, 200), random.randint(-200, 200)], 55, fill="orange", outline="white", width=3)


def change_circle_color():
    if circle1 == False:
        g.la(text="You must make the circle first")
        return
    try:
        color = entry.get()
        circle1.config(fill=str(color))
    except:
        g.la(text="Please enter a valid color")
        return


canvas = g.ca(500, 500, bg="black")
g.bu(text="make me a circle", command=make_circle)
entry = g.en(text="name a color")
g.bu(text="change circle color to entry", command=change_circle_color)


g.mainloop()

