"""Write an add method for the Point class."""

class Point(object):
    def __init__(self, x=45, y=50):
        self.x = x
        self.y = y
    def __str__(self):
        return '%s, %s' % (self.x, self.y)
    def add_point(self, other):
        new_point = Point(self.x + other.x, self.y + other.y)
        return new_point


p = Point()

t = Point(20, 30)

print p + t