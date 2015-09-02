"""To choose a random word from the histogram, the simplest algorithm is to
build a list with multiple copies of each word, according to the observed frequency,
and then choose from the list:

def random_word(h):
    t = []
    for word, freq in h.items():
        t.extend([word] * freq)

    return random.choice(t)
The expression [word] * freq creates a list with freq copies of the string word.
The extend method is similar to append except that the argument is a sequence.
Exercise 7
This algorithm works, but it is not very efficient; each time you choose a random
word, it rebuilds the list, which is as big as the original book. An obvious improvement
is to build the list once and then make multiple selections, but the list is still big.
An alternative is:

Use keys to get a list of the words in the book.
Build a list that contains the cumulative sum of the word frequencies (see Exercise 3).
The last item in this list is the total number of words in the book, n.
Choose a random number from 1 to n. Use a bisection search (See Exercise 11) to find
the index where the random number would be inserted in the cumulative sum.

Use the index to find the corresponding word in the word list.
Write a program that uses this algorithm to choose a random word from the book."""

import string
from bisect import bisect
import random


def make_word_count_dict(a_file, start_line=1):
    new_text = []
    fin = open(a_file)
    lines = fin.readlines()
    lines = lines[start_line - 1:]

    for line in lines:
        stripped_line = line.strip().lower().translate(string.maketrans("",""), string.punctuation).split()
        new_text += stripped_line

    word_count_dict = {}
    for word in new_text:
        word_count_dict[word] = word_count_dict.get(word, 0) + 1

    return word_count_dict



def cumulative_sum(num_list):
    sum_list = []
    preceding_count = 0

    for num in num_list:
        num += preceding_count
        sum_list.append(num)
        preceding_count = num

    return sum_list


def random_word_from_histo(histogram):
    words = []
    freqs = []

    sorted_count = sorted([(v, k) for k, v in histogram.iteritems()])

    for freq, word in sorted_count:
        words += [word]
        freqs += [freq]


    cumulative_freqs = cumulative_sum(freqs)
    cumulative_total = cumulative_freqs[-1]

    random_num = random.randint(0, cumulative_total -1)
    index = bisect(cumulative_freqs, random_num)

    return words[index]
