"""Write a function that reads the words in words.txt and stores
them as keys in a dictionary. It doesn’t matter what the values are.
Then you can use the in operator as a fast way to check whether a
string is in the dictionary.
If you did Exercise 11, you can compare the speed of this implementation
with the list in operator and the bisection search."""

def make_word_list(file):
    word_list = open(file)
    list = []
    for line in word_list:
        word = line.strip()
        list += [word]
    return list

wordlist = make_word_list("words.txt")


def make_dictionary(list):
    word_dict = dict()
    for word in list:
        word_dict[word] = ''
    return word_dict


dictlist = make_dictionary(wordlist)


def check_for_string(word, dictionary):
    return word in dictionary


