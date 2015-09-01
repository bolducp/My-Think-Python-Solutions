""" Write a function called is_sorted that takes a list as a
parameter and returns True if the list is sorted in ascending
order and False otherwise. You can assume (as a precondition)
that the elements of the list can be compared with the relational
operators <, >, etc.
For example, is_sorted([1,2,2]) should return True and is_sorted(['b','a'])
should return False."""


def is_sorted(a_list):
    if a_list == sorted(a_list):
        return True
    return False


#OR (simplified)

def is_sorted2(a_list):
    return a_list == sorted(a_list)


#OR (not using the built-in sorted function)

def is_sorted3(a_list):
    for num in range(len(a_list) - 1):
        if a_list[num] > a_list[num + 1]:
            return False
    return True

