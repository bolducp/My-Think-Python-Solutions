"""Write a function that takes a string as an argument and displays
the letters backward, one per line."""

def display_backwards(string):
    index = len(string) - 1
    while index > -1:
        letter = string[index]
        print letter
        index -= 1

#alternatively:

def display_backwards_2(string):
    for letter in string[::-1]:
        print letter


