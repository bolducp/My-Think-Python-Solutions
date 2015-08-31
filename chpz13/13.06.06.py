"""Python provides a data structure called set that provides
many common set operations. Read the documentation at
http://docs.python.org/2/library/stdtypes.html#types-set and
write a program that uses set subtraction to find words in
the book that are not in the word list. """


import string

def make_wordlist(file):
    result = []
    wordlist = open(file)
    for line in wordlist:
        word = line.strip()
        result += [word]
    return result

wordlist = make_wordlist("words.txt")


def find_words_not_in_wordlist2(a_file, wordlist, start_line=1):
    new_text = []
    fin = open(a_file)
    lines = fin.readlines()
    lines = lines[start_line - 1:]
    punctuations = string.punctuation
    punctuations = punctuations.replace("-", "")

    for line in lines:
        stripped_line = line.strip().lower().replace("--", " ").translate(string.maketrans("", ""), punctuations).split()
        new_text += stripped_line

    word_count_dict = {}
    for word in new_text:
        word_count_dict[word] = word_count_dict.get(word, 0) + 1

    not_in_wordlist = list(set(word_count_dict.keys()) - set(wordlist))

    return not_in_wordlist

