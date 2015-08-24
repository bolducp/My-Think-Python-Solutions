import math

def square_root(a):
    a = float(a)
    x = a/2
    while True:
        y = (x + a/x) / 2
        if x == y:
            break
        x = y
    return x

def square_root_table(n_range):
    for num in range(1, n_range):
        print num,
        print square_root(num),
        print math.sqrt(num),
        print abs(square_root(num) - math.sqrt(num))