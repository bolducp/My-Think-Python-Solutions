"""Write a function called middle that takes a list and
returns a new list that contains all but the first and
last elements. So middle([1,2,3,4]) should return [2,3]."""

def middle(list):
    del list[0]
    del list[len(list) - 1]
    return list

#OR

def middle_2(list):
    return list[1:-1]

