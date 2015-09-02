"""If you download my solution to Exercise 4 from
http://thinkpython.com/code/anagram_sets.py, you’ll see that it creates a
dictionary that maps from a sorted string of letters to the list of words
that can be spelled with those letters. For example, ’opst’ maps to the list
[’opts’, ’post’, ’pots’, ’spot’, ’stop’, ’tops’].
Write a module that imports anagram_sets and provides two new functions:
store_anagrams should store the anagram dictionary in a “shelf;” read_anagrams
should look up a word and return a list of its anagrams. """


from downey_anagram import *
import shelve


def store_anagrams(filename, anagram_file):
    anagram_dict = all_anagrams(anagram_file)
    anagram_shelve = shelve.open(filename)

    for key in anagram_dict.keys():
        anagram_shelve[key] = anagram_dict[key]

    anagram_shelve.close()


def read_anagrams(filename, a_word):
    anagram_shelve = shelve.open(filename)

    sig = signature(a_word)
    return anagram_shelve[sig]

