"""To check whether a word is in the word list, you could use the in
operator, but it would be slow because it searches through the words in order.
Because the words are in alphabetical order, we can speed things up with
a bisection search (also known as binary search), which is similar to what
you do when you look a word up in the dictionary. You start in the middle
and check to see whether the word you are looking for comes before the
word in the middle of the list. If so, then you search the first half of
the list the same way. Otherwise you search the second half.

Either way, you cut the remaining search space in half. If the word list
has 113,809 words, it will take about 17 steps to find the word or conclude
that it’s not there.

Write a function called bisect that takes a sorted list and a target value
and returns the index of the value in the list, if it’s there, or None if it’s not.

Or you could read the documentation of the bisect module and use that!"""


def make_wordlist(file):
    list = []
    wordlist = open(file)
    for line in wordlist:
        word = line.strip()
        list += [word]
    return list

wordlist = make_wordlist("words.txt")


def bisect(sorted_list, target_value):
    max_high = len(sorted_list) - 1
    min_low = 0
    index = (len(sorted_list) - 1) / 2

    while True:
        if sorted_list[index] == target_value:
            return index
        elif max_high < min_low:
            return None
        elif sorted_list[index] < target_value:
            min_low = index + 1
        else:
            max_high = index - 1

        index = (max_high + min_low) / 2

print bisect(wordlist, "open")