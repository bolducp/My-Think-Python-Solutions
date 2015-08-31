"""In this example:

def sort_by_length(words):
    t = []
    for word in words:
       t.append((len(word), word))

    t.sort(reverse=True)

    res = []
    for length, word in t:
        res.append(word)
    return res

ties are broken by comparing words, so words with the same
length appear in reverse alphabetical order. For other applications
you might want to break ties at random. Modify this example so
that words with the same length appear in random order.
Hint: see the random function in the random module."""


import random

def sort_by_length(words):
    t = []
    for word in words:
       t.append((len(word), random.randint(1, 10), word))

    t.sort(reverse=True)

    res = []
    for length, randomint, word in t:
        res.append(word)
    return res