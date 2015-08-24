"""Write a function called is_palindrome that takes a string argument
and returns True if it is a palindrome and False otherwise.
Remember that you can use the built-in function len to check the length of a string."""

def is_palidrome(word):
    return word == word[::-1]

