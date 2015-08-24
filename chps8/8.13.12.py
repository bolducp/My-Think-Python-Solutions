"""ROT13 is a weak form of encryption that involves “rotating” each letter
in a word by 13 places. To rotate a letter means to shift it through the alphabet,
wrapping around to the beginning if necessary, so ’A’ shifted by 3 is ’D’ and
’Z’ shifted by 1 is ’A’.

Write a function called rotate_word that takes a string and an integer as parameters,
and that returns a new string that contains the letters from the original
string “rotated” by the given amount."""


def rotate_word(string, n):
    lower_string = string.lower()
    num_string = []
    new_string = ''

    for char in lower_string:
        num_char = ord(char) - 96 + n
        num_string.append(num_char)

    for num in num_string:
        new_char = chr(96 + (num % 26))
        new_string += new_char

    return new_string