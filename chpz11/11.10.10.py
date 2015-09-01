"""Two words are “rotate pairs” if you can rotate one of them and get
the other (see rotate_word in Exercise 12).
Write a program that reads a wordlist and finds all the rotate pairs."""


def rotate_word(string, n):
    lower_string = string.lower()
    num_string = []
    new_string = ''

    for char in lower_string:
        num_char = ord(char) - 96 + n
        num_string.append(num_char)

    for num in num_string:
        new_char = chr(96 + (num % 26))
        new_string += new_char

    return new_string


def make_dictionary(file):
    word_dict = {}
    wordlist = open(file)
    for line in wordlist:
        word = line.strip().lower()
        word_dict[word] = []
    return word_dict

word_dict = make_dictionary("words.txt")


def find_rotate_pairs(dictionary):
    rotate_pairs = []
    for item in dictionary:
        for num in range(1, 26):
            rotate = rotate_word(item, num)
            if rotate in dictionary:
                rotate_pairs += ['rotate ' + str(num) + ': ' + item + ' / ' + rotate]
    return rotate_pairs

print find_rotate_pairs(word_dict)