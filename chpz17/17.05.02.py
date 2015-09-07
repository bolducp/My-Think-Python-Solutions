"""Write an init method for the Point class that takes x and y as
optional parameters and assigns them to the corresponding attributes."""


class Point(object):
    def __init__(self, x=45, y=50):
        self.x = x
        self.y = y

