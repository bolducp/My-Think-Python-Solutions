def print_it():
    print "hello"

def do_n(a_function, n):
    if n <= 0:
        return
    a_function()
    do_n(a_function, n-1)

do_n(print_it, 10)
