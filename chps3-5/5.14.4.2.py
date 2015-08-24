
def is_triangle(side_a, side_b, side_c):
    if (side_a + side_b) < side_c or (side_b + side_c) < side_a or (side_a + side_c) < side_b:
        print "No"
    else:
        print "Yes"

def get_values_and_check_is_triangle():
    side_a = int(raw_input("What is the length of side a?\n"))
    side_b = int(raw_input("What is the length of side b?\n"))
    side_c = int(raw_input("What is the length of side c?\n"))
    is_triangle(side_a, side_b, side_c)
