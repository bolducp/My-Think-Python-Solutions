
def is_power(a, b):
    if a == b:
        return True
    elif a % b == 0:
        if is_power(float(a)/float(b), float(b)):
            return True
        else:
            return False
    else:
        return False

