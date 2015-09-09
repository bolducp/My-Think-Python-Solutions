"""Download my code from Section 13.8 (http://thinkpython.com/code/markov.py), and follow the steps
 described above to encapsulate the global variables as attributes of a new class called Markov."""

import string
import random


class Markov(object):
    def __init__(self, start_line, order):
        self.suffix_map = {}
        self.prefix = ()
        self.start_line = start_line
        self.order = order


    def process_word(self, word):
        if len(self.prefix) < self.order:
            self.prefix += (word,)
            return

        try:
            self.suffix_map[self.prefix].append(word)

        except KeyError:
            # if there is no entry for this prefix, make one
            self.suffix_map[self.prefix] = [word]

        self.prefix = shift(self.prefix, word)



    def random_text(self, n):
        start = random.choice(self.suffix_map.keys())
        print "start", start

        for i in range(n):
            suffixes = self.suffix_map.get(start, None)
            if suffixes == None:
                print "None here"
                # if the start isn't in map, we got to the end of the
                # original text, so we have to start again.
                random_text(n-1)
                return

            # choose a random suffix
            word = random.choice(suffixes)
            print word,
            start = shift(start, word)


def process_file(a_file, markov_obj):
    fin = open(a_file)
    lines = fin.readlines()
    lines = lines[markov_obj.start_line - 1:]
    punctuations = string.punctuation
    punctuations = punctuations.replace(".", "")

    for line in lines:
        for word in line.strip().replace("--", " ").translate(string.maketrans("", ""), punctuations).split():
            markov_obj.process_word(word)


def shift(t, word):
    return t[1:] + (word,)


def main(filename='', start_line=1,order=2, n=100):
    n = int(n)
    order = int(order)
    markov_obj = Markov(start_line, order)
    process_file(filename, markov_obj)
    markov_obj.random_text(n)


print main("jane.txt", 71)