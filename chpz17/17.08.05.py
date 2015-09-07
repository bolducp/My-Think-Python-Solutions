"""Write an add method for Points that works with either a Point object
or a tuple:
If the second operand is a Point, the method should return a new
Point whose x coordinate is the sum of the x coordinates of the
operands, and likewise for the y coordinates.

If the second operand is a tuple, the method should add the first
element of the tuple to the x coordinate and the second element to
the y coordinate, and return a new Point with the result."""


class Point(object):

    def __init__(self, x=45, y=50):
        self.x = x
        self.y = y

    def __str__(self):
        return '%s, %s' % (self.x, self.y)

    def __add__(self, other):
        if isinstance(other, Point):
            return self.add_point(other)
        else:
            return self.add_tuple(other)

    def add_point(self, other):
        new_point = Point(self.x + other.x, self.y + other.y)
        return new_point

    def add_tuple(self, t):
        new_point = Point(self.x + t[0], self.y + t[1])
        return new_point

    def __radd__(self, other):
        return self.__add__(other)


def print_attributes(obj):
    for attr in obj.__dict__:
        print attr, getattr(obj, attr)


p = Point(45, 50)
r = Point(-20, -5)

print p + (38, 40)
print p + r
