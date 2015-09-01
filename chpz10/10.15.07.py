"""Two words are anagrams if you can rearrange the letters
from one to spell the other. Write a function called is_anagram
that takes two strings and returns True if they are anagrams."""


def is_anagram(word1, word2):
    return sorted(word1.replace(" ","")) == sorted(word2.replace(" ",""))


#OR

def is_anagram2(word1, word2):
    word1 = list(word1.replace(" ",""))
    word2 = list(word2.replace(" ",""))

    for letter in word1:
        if letter not in word2:
            return False

    while len(word1) > 0 and len(word2) > 0:
        for letter in word1:
            word1.remove(letter)
            word2.remove(letter)

    if len(word1) == 0 and len(word2) == 0:
        return True
    return False
