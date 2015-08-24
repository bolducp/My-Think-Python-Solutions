
def check_fermat(a, b, c, n):
    if n <=2:
        print "n must be greater than 2"
        return
    elif a**n + b**n == c**n:
         print "Holy smokes, Fermat was wrong!"
    else:
        print "No, that doesn't work."

#Alternatively:

def check_fermat2(a, b, c, n):
    if n > 2 and a**n + b**n == c**n:
        print "Holy smokes, Fermat was wrong!"
    else:
        print "No, that doesn't work."

