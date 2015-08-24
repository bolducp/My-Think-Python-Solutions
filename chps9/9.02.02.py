"""Write a function called has_no_e that returns True if the given word
doesn’t have the letter “e” in it.

Modify your program from the previous section to print only the words
that have no “e” and compute the percentage of the words in the list have no “e.”"""

fin = open("words.txt")

def has_no_e():
    total_count = 0
    no_e_count = 0

    for line in fin:
        word = line.strip()
        if "e" not in word:
            no_e_count += 1
            print word
        total_count += 1

    no_e_percentage = float(no_e_count) / total_count * 100
    return no_e_percentage

#alternatively, maybe this is closer to what Downey had in mind when he says,
#“Write a function called has_no_e that returns True if the given word doesn’t
# have the letter “e” in it.” The two separate function names at least seem
# more accurate here, I think.


fin = open("words.txt")

def has_no_e(word):
    return "e" not in word

def calculate_no_e_percentage():
    total_count = 0
    no_e_count = 0

    for line in fin:
        word = line.strip()
        if has_no_e(word):
            no_e_count += 1
            print word
        total_count += 1

    no_e_percentage = float(no_e_count) / total_count * 100
    return no_e_percentage

print calculate_no_e_percentage()