"""Use capitalize_all to write a function named capitalize_
nested that takes a nested list of strings and returns a
new nested list with all strings capitalized."""

#Downey's "capitalize all" function:

def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

#my solution utilizing "capitalize all":

def capitalize_nested(list_of_strings):
    final_list = []
    for item in list_of_strings:
        if type(item) == str:
            final_list.append(capitalize_all(item))
        else:
            final_list.append(capitalize_nested(item))

    return final_list

print capitalize_nested(sample_list)