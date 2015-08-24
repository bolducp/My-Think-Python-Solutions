
def check_fermat(a, b, c, n):
    if n > 2 and a**n + b**n == c**n:
        print "Holy smokes, Fermat was wrong!"
    else:
        print "No, that doesn't work."

def get_values_and_check_fermat():
    a = int(raw_input("What is the value of a?\n"))
    b = int(raw_input("What is the value of b?\n"))
    c = int(raw_input("What is the value of c?\n"))
    n = int(raw_input("What is the value of n?\n"))
    check_fermat(a, b, c, n)

get_values_and_check_fermat()



