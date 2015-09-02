"""Here’s another Car Talk Puzzler (http://www.cartalk.com/content/puzzlers):

What is the longest English word, that remains a valid English word, as
you remove its letters one at a time?
Now, letters can be removed from either end, or the middle, but you can’t
rearrange any of the letters. Every time you drop a letter, you wind up with
another English word. If you do that, you’re eventually going to wind up with
one letter and that too is going to be an English word—one that’s found in
the dictionary. I want to know what’s the longest word and how many letters does it have?
I’m going to give you a little modest example: Sprite. Ok? You start off with
sprite, you take a letter off, one from the interior of the word, take the r
away, and we’re left with the word spite, then we take the e off the end, we’re
left with spit, we take the s off, we’re left with pit, it, and I.

Write a program to find all words that can be reduced in this way, and then
find the longest one.

This exercise is a little more challenging than most, so here are some suggestions:

You might want to write a function that takes a word and computes a list of all
the words that can be formed by removing one letter. These are the “children” of the word.
Recursively, a word is reducible if any of its children are reducible. As a base case,
you can consider the empty string reducible.
The wordlist I provided, words.txt, doesn’t contain single letter words. So you might
want to add “I”, “a”, and the empty string.
To improve the performance of your program, you might want to memoize the words that
are known to be reducible."""


from bisect import bisect_left

def make_wordlist(file):
    result = []
    wordlist = open(file)
    for line in wordlist:
        word = line.strip()
        result += [word]
    return result


def in_bisect(word_list, word):
    i = bisect_left(word_list, word)
    return i != len(word_list) and word_list[i] == word


known_children = {}
known_reducibles = []

def get_children(a_word, wordlist):
    if len(a_word) == 1:
        return []

    if a_word in known_children:
        return known_children[a_word]

    children = []
    for i in range(len(a_word)):
        new_word = str(a_word[:i]) + str(a_word[i + 1:])
        if in_bisect(wordlist, new_word):
            children.append(new_word)
    known_children[a_word] = children
    return children


def is_reducible(a_word, wordlist):
    if a_word in known_reducibles:
        return True

    children = get_children(a_word, wordlist)

    if a_word == "i" or a_word == "a":
        return True

    elif not children:
        return False

    for child in children:
        if is_reducible(child, wordlist):
            known_reducibles.append(child)
            return True
    return False


def find_longest_reducible(wordlist):
    longest = ''
    for word in wordlist:
        if len(word) > len(longest) and is_reducible(word, wordlist):
            longest = word
    return longest
