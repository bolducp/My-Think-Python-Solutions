"""Read the documentation of the dictionary method setdefault
and use it to write a more concise version of invert_dict."""


def rewritten_histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d


def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        inverse.setdefault(val, [])
        inverse[val].append(key)
    return inverse
