"""Write a function named uses_all that takes a word and a string of required letters,
and that returns True if the word uses all the required letters at least once.
How many words are there that use all the vowels aeiou? How about aeiouy?"""

def uses_all(word, string):
    for char in string:
        if char not in word:
            return False
    return True

wordlist = open("words.txt")

def find_words_using_req_letters():
    using_req_letters = 0
    req_letters = raw_input("What are the required letters?")
    req_letters = req_letters.lower()

    for line in wordlist:
        word = line.strip()
        if uses_all(word, req_letters):
            print word
            using_req_letters += 1
    return using_req_letters

find_words_using_req_letters()

