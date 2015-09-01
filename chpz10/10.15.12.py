"""Two words are a “reverse pair” if each is the reverse of the other.
Write a program that finds all the reverse pairs in the word list."""


from bisect import bisect_left

def make_wordlist():
    wordlist = open("words.txt")
    list = []
    for line in wordlist:
        word = line.strip()
        list += [word]
    return list

wordlist = make_wordlist()


#the following function was introduced by Downey in the previous exercise:

def in_bisect(word_list, word):
    i = bisect_left(word_list, word)
    if i != len(word_list) and word_list[i] == word:
        return True
    else:
        return False

def find_reverse_pairs(word_list):
    reverse_pairs = []
    count = 0
    for word in word_list:
        if in_bisect(word_list, word[::-1]):
            reverse_pairs.append(word + "/" + word[::-1])
            count += 1
    print "Number of reverse pairs: " + str(count)
    return reverse_pairs

find_reverse_pairs(wordlist)

