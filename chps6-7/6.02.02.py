"""Use incremental development to write a function called hypotenuse
that returns the length of the hypotenuse of a right triangle given
the lengths of the two legs as arguments."""

import math

def hypotenuse(leg_a, leg_b):
    a_squared = leg_a**2
    b_squared = leg_b**2
    hypotenuse_squared = a_squared + b_squared
    hypotenuse = math.sqrt(hypotenuse_squared)
    return hypotenuse

#alternatively:

def hypotenuse2(leg_a, leg_b):
    return math.sqrt(leg_a**2 + leg_b**2)

