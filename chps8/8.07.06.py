"""Rewrite this function (i.e. 8.07.05) so that instead of traversing the string,
 it uses the three-parameter version of find from the previous section."""

#I struggled with this exercise for a long time.
#I kept wanting to re-write the "three-parameter version of the 'find'
#function" to be more useful for counting the number of occurrences.
#I think what I've ended up with is pretty messy.


def find(word, letter, starting_index):
    index = starting_index
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    return -1

def count_new(string, letter):
    count = 0
    starting_index = 0
    while starting_index < len(string):
        if find(string, letter, starting_index) == -1:
            print "None"
            break
        else:
            count += 1
            starting_index = find(string, letter, starting_index) + 1
    return count