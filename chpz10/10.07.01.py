"""Write a function called nested_sum that takes a nested list
of integers and add up the elements from all of the nested lists."""

def nested_sum(list):
    total = 0
    for item in list:
        if type(item) == int:
            total += item
        else:
            inner_list_total = nested_sum(item)
            total += inner_list_total
    return total