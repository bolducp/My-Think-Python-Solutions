"""Modify reverse_lookup so that it builds and returns a list of all
keys that map to v, or an empty list if there are none."""

def reverse_lookup(d, v):
    list_v = []
    for k in d:
        if d[k] == v:
            list_v += [k]
    return list_v

