"""Write a function named uses_only that takes a word and a string of letters,
and that returns True if the word contains only letters in the list."""

wordlist = open("words.txt")

def uses_only(word, string):
    for char in word:
        if char not in string:
            return False
    return True


def find_words_using_only_letters():
    uses_only_count = 0
    uses_only_string = raw_input("what are the acceptable letters?")
    for line in wordlist:
        word = line.strip()
        if uses_only(word, uses_only_string):
            print word
            uses_only_count += 1
    print uses_only_count

find_words_using_only_letters()
