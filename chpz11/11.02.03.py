"""Dictionaries have a method called keys that returns the keys of the
dictionary, in no particular order, as a list.

Modify print_hist to print the keys and their values in alphabetical order."""


def rewritten_histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d


def print_hist(h):
    key_list = sorted(h.keys())
    for key in key_list:
        print key, h[key]

