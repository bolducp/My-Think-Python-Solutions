"""Write a version of move_rectangle (from 15.05.02)
that creates and returns a new Rectangle instead of
modifying the old one."""


import copy

class Point(object):
    "represents a point in 2-D space"

class Rectangle(object):
    """Represents a rectangle.

    attributes: width, height, corner"""

def move_rectangle(rect, dx, dy):
    new_rect = copy.deepcopy(rect)

    new_rect.corner.x = rect.corner.x + dx
    new_rect.corner.y = rect.corner.y + dy
    return new_rect


box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

print box.corner.x
print box.corner.y

new_rect = move_rectangle(box, 3.0, 3.0)

print new_rect.corner.x
print new_rect.corner.y
