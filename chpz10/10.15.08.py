"""he (so-called) Birthday Paradox:
#1. Write a function called has_duplicates that takes a list and
returns True if there is any element that appears more than
once. It should not modify the original list.

#2. If there are 23 students in your class, what are the chances
that two of you have the same birthday? You can estimate this
probability by generating random samples of 23 birthdays and
checking for matches. Hint: you can generate random birthdays
with the randint function in the random module."""


#Part 1
import random

def has_duplicates(a_list):
    for item in a_list:
        if a_list.count(item) >= 2:
            return True
    return False



#Part 2

def generate_birthdays(num_students):
    student_birthdays = []
    for student in range(num_students):
        student_birthdays.append(random.randint(1, 365))
    return student_birthdays


def calculate_percent_bday_matches(num_students, times_to_run):
    num_matches = 0

    for i in range(times_to_run):
        student_birthdays = generate_birthdays(num_students)
        if has_duplicates(student_birthdays):
            num_matches += 1

    percent_matches = float(num_matches) / times_to_run * 100
    return percent_matches

print calculate_percent_bday_matches(23, 1)
