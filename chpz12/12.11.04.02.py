"""Modify the previous program (12.11.04.01) so that it prints the largest
set of anagrams first, followed by the second largest set, and so on."""


def find_anagrams(list_words):
    d = {}
    for item in list_words:
        letters = []
        for letter in item:
            letters += letter
        r = tuple(sorted(letters))
        if r in d:
            d[r].append(item)
        else:
            d[r] = [item]

    anagrams = []
    for item in d.values():
        if len(item) > 1:
            anagrams += [item]

    sorted_anagrams = sorted(anagrams, key=len, reverse=True)
    return sorted_anagrams