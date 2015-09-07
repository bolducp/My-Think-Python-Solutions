"""Write a str method for the Point class. Create a Point object and
print it."""


class Point(object):
    def __init__(self, x=45, y=50):
        self.x = x
        self.y = y
    def __str__(self):
        return '%s, %s' % (self.x, self.y)

p = Point()

print p

