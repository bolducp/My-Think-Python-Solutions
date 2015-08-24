"""Give me a word with three consecutive double letters. I’ll give you a
couple of words that almost qualify, but don’t. For example, the word committee,
 c-o-m-m-i-t-t-e-e. It would be great except for the ‘i’ that sneaks in there.
 Or Mississippi: M-i-s-s-i-s-s-i-p-p-i. If you could take out those i’s it would
work. But there is a word that has three consecutive pairs of letters and to the
best of my knowledge this may be the only word. Of course there are probably 500
more but I can only think of one. What is the word?"""

def has_triple_double(word):
    for i in range(len(word) - 5):
            if word[i] == word[i + 1]:
                if word[i + 2] == word[i + 3]:
                    if word[i + 4] == word[i + 5]:
                        return True
    return False

wordlist = open("words.txt")

def find_triple_doubles():
    for line in wordlist:
        word = line.strip()
        if has_triple_double(word):
            print word

find_triple_doubles()

