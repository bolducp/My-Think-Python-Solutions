
def is_triangle(side_a, side_b, side_c):
    if (side_a + side_b) < side_c or (side_b + side_c) < side_a or (side_a + side_c) < side_b:
        print "No"
    else:
        print "Yes"