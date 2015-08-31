"""Modify the program from the previous exercise to print
the 20 most frequently-used words in the book."""

import string

def top_20_frequent_words(a_file, start_line=1):
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

    sorted_count = sorted([(v, k) for k, v in word_count_dict.iteritems()], reverse=True)
    top_20 = sorted_count[:20]

    for count, word in top_20:
        print word + " : " + str(count)

