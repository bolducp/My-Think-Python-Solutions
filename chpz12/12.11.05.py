"""Two words form a “metathesis pair” if you can transform one
into the other by swapping two letters; for example, “converse”
and “conserve.” Write a program that finds all of the metathesis
pairs in the dictionary. Hint: don’t test all pairs of words, and
don’t test all possible swaps. """

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
    return d

def anagram_is_metathesis(word1, word2):
    difference_count = 0
    for a, b in zip(word1, word2):
        if a != b:
            difference_count += 1
    return difference_count == 2

def find_metathesis_pairs(a_list):
    a_dict = find_anagrams(a_list)

    metathesis_pairs = []
    for value in a_dict.values():
        if len(value) > 1:
            words = value

            for x in words:
                for y in words:
                    if anagram_is_metathesis(x, y):
                        metathesis_pairs += [x + " / " + y]
    return metathesis_pairs





