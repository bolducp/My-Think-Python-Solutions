"""Write a function named choose_from_hist that takes a
histogram as defined in Section 11.1 and returns a random
value from the histogram, chosen with probability in proportion
to frequency. For example, for this histogram:

>>> t = ['a', 'a', 'b']
>>> hist = histogram(t)
>>> print hist
{'a': 2, 'b': 1}
your function should return ’a’ with probability 2/3 and
’b’ with probability 1/3."""

import random

def choose_from_histogram(a_hist):
    choice_list = []
    for k in a_hist:
        for num in range(a_hist[k]):
            choice_list += k

    random_choice = random.choice(choice_list)
    return random_choice
