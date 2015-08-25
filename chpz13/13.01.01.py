"""Write a program that reads a file, breaks each line
into words, strips whitespace and punctuation from the words,
and converts them to lowercase."""

import string

def stripped_text(a_file):
    new_text = []
    fin = open(a_file)

    for line in fin:
        stripped_line = line.lower().translate(string.maketrans("",""), string.punctuation).split()
        new_text += stripped_line
    return new_text



print stripped_text("jane.txt")
