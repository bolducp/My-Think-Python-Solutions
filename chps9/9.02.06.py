"""Write a function called is_abecedarian that returns True if the letters in a word appear
in alphabetical order (double letters are ok). How many abecedarian words are there?"""

def is_abecedarian(word):
    inital_letter = word[0]
    next_letter = word[1]
    next_letter_index = 1

    while next_letter_index < next_letter:
            return False
        inital_letter = next_letter
        next_letter_index += 1
        next_letter = word[next_letter_index]
    return True


wordlist = open("words.txt")

def calculate_abecedarian():
    total_count = 0
    for word in wordlist:
        if is_abecedarian(word):
            print word,
            total_count += 1
    return total_count

calculate_abecedarian()