"""Write a function that reads the file words.txt and builds a list
with one element per word. Write two versions of this function,
one using the append method and the other using the idiom t = t + [x].
Which one takes longer to run? Why?
Hint: use the time module to measure elapsed time."""


import time

def make_word_list(file):
    wordlist = []
    wordfile = open(file)
    for word in wordfile:
        word = word.strip()
        wordlist.append(word)
    wordfile.close()
    return wordlist


def make_word_list2(file):
    wordlist = []
    wordfile = open(file)
    for word in wordfile:
        word = word.strip()
        wordlist += [word]
    return wordlist


start_time = time.clock()
make_word_list("words.txt")
end_time = time.clock()
print "Appending to make list time: " + str(end_time - start_time)


start_time = time.clock()
make_word_list2("words.txt")
end_time = time.clock()
print "Concatenating to make list time: " + str(end_time - start_time)

#Concatenating is faster
