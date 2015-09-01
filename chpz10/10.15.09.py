"""Write a function called remove_duplicates that takes a list and
returns a new list with only the unique elements from the original.
Hint: they don’t have to be in the same order."""

def remove_duplicates(a_list):
    new_list = []
    for item in a_list:
        if item not in new_list:
            new_list.append(item)
    return new_list

