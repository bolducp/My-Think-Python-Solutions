"""Rewrite the function print_n from Section 5.8 using iteration instead of recursion.
5.8 function:
def countdown(n):
    if n <= 0:
        print ‘Blastoff!’
    else:
        print n
countdown(n-1)"""


def countdown(n):
    while n > 0:
        print n
        n -= 1
    print "Blastoff!"