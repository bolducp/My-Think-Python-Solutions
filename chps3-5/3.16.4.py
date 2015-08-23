def do_twice(f, val):
    f(val)
    f(val)

def print_twice(some_string):
    print some_string
    print some_string
    
do_twice(print_twice, 'spam')
 
def do_four(f, val):
    do_twice(f, val)
    do_twice(f, val)
    
do_four(print_twice, 'spam2')