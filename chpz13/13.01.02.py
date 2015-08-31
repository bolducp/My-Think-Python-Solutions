"""Go to Project Gutenberg (http://gutenberg.org) and download your favorite
out-of-copyright book in plain text format.
Modify your program from the previous exercise to read the book you downloaded,
skip over the header information at the beginning of the file, and process the
rest of the words as before.

Then modify the program to count the total number of words in the book, and the
number of times each word is used.

Print the number of different words used in the book. Compare different books
by different authors, written in different eras. Which author uses the most
extensive vocabulary?"""


import string

def vocabulary_counter(a_file, start_line=1):
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

    total_words = len(new_text)
    num_different_words = len(word_count_dict.keys())
    varied_vocab_percent = float(num_different_words) / total_words

    print "Total number of words: " + str(total_words) + "\n" + "Number of different words: " + str(num_different_words) + "\n" + "Vocab Variance Percent: " + str(varied_vocab_percent)





