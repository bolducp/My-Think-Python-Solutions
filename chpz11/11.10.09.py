"""If you did Exercise 8, you already have a function named has_duplicates
that takes a list as a parameter and returns True if there is any object
that appears more than once in the list.

Use a dictionary to write a faster, simpler version of has_duplicates."""


def has_duplicates2(a_list):
    duplicates_dict = dict()
    for item in a_list:
        duplicates_dict[item] = duplicates_dict.get(item, 0) + 1
    for key in duplicates_dict:
        return duplicates_dict[key] >=2

