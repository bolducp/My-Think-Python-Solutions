"""Write a function called most_frequent that takes a string
and prints the letters in decreasing order of frequency."""


def most_frequent(a_string):
    a_string = a_string.replace(" ", "")
    print a_string
    frequencies = {}
    for letter in a_string:
        frequencies[letter] = frequencies.get(letter, 0) + 1

    results = []

    for letter, freq in frequencies.items():
        results += [(freq, letter)]
    results.sort(reverse=True)

    for freq, letter in results:
        print letter, freq

