import string
from bisect import bisect_left

ex_list = [1, 10, 15]

def cumulative_sum(num_list):
    sum_list = []
    preceding_count = 0

    for num in num_list:
        num += preceding_count
        sum_list.append(num)
        preceding_count = num

    return sum_list

print cumulative_sum(ex_list)




def in_bisect(word_list, word):
    i = bisect_left(word_list, word)
    return i != len(word_list) and word_list[i] == word




def get_words_in_file(a_file, start_line=1):
    new_text = []
    fin = open(a_file)
    lines = fin.readlines()
    lines = lines[start_line - 1:]
    punctuations = string.punctuation
    punctuations = punctuations.replace("-", "")

    for line in lines:
        stripped_line = line.strip().lower().replace("--", " ").translate(string.maketrans("", ""), punctuations).split()
        new_text += stripped_line

    word_count_dict = {}
    for word in new_text:
        word_count_dict[word] = word_count_dict.get(word, 0) + 1

    words = []
    for key in word_count_dict:
        words += [key]
    return words

print get_words_in_file("smalljane.txt")

 sum_freq = cumulative_sum( .values())