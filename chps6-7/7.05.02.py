
def square_root(a):
    x = float(a/2)
    while True:
        y = (x + a/x) / 2
        if y == x:
            break
        x = y
    return x
