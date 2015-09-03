"""Write a function named move_rectangle that takes a
Rectangle and two numbers named dx and dy. It should
change the location of the rectangle by adding dx to
the x coordinate of corner and adding dy to the y
coordinate of corner."""


class Point(object):
    "represents a point in 2-D space"

class Rectangle(object):
    """Represents a rectangle.

    attributes: width, height, corner"""

def move_rectangle(rect, dx, dy):
    rect.corner.x += dx
    rect.corner.y += dy

box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

print box.corner.x
print box.corner.y

move_rectangle(box, 3.0, 3.0)

print box.corner.x
print box.corner.y
