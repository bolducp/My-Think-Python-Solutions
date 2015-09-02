"""Markov analysis:
Write a program to read a text from a file and perform Markov analysis.
The result should be a dictionary that maps from prefixes to a collection
of possible suffixes. The collection might be a list, tuple, or dictionary;
it is up to you to make an appropriate choice. You can test your program with
prefix length two, but you should write the program in a way that makes it
easy to try other lengths.

Add a function to the previous program to generate random text based on the
Markov analysis."""

import random
import string


def make_list_of_words_from_file(a_file, start_line=1):
    fin = open(a_file)
    lines = fin.readlines()
    lines = lines[start_line - 1:]
    new_text = []

    for word in lines:
        new_text += word.split()

    return new_text


def make_word_list(a_file, start_line=1):
    new_text = []
    fin = open(a_file)
    lines = fin.readlines()
    lines = lines[start_line - 1:]
    punctuations = string.punctuation
    punctuations = punctuations.replace(".", "")

    for line in lines:
        stripped_line = line.strip().lower().replace("--", " ").translate(string.maketrans("", ""), punctuations).split()
        new_text += stripped_line
    return new_text



def make_suffix_dict(a_list, prefix_len=2):
    suffix_dict = {}

    for index in range(len(a_list) - prefix_len - 1):
        prefix = a_list[index: index + prefix_len]
        prefix = ' '.join(prefix)
        suffix = a_list[index + prefix_len + 1]

        if prefix in suffix_dict:
            suffix_dict[prefix].append(suffix)
        else:
            suffix_dict[prefix] = [suffix]
    return suffix_dict



def generate_random_text(suffix_dict, num_chars=100, prefix_length=2):

    start_text = random.choice(suffix_dict.keys())
    sample_text = start_text

    for i in range(num_chars):
        try:
            next_word = random.choice(suffix_dict[sample_text[-prefix_length:]])
        except:
            next_word = random.choice(suffix_dict.keys())
        sample_text += " " + next_word

    return sample_text



def main(a_file, start_line=1, prefix_length=2, num_chars=100):
    list_words = make_word_list(a_file, start_line)
    suffix_dict = make_suffix_dict(list_words, prefix_length)
    random_text = generate_random_text(suffix_dict, num_chars, prefix_length)
    return random_text
