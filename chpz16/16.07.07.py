"""The datetime module provides date and time objects that are similar
to the Date and Time objects in this chapter, but they provide a rich
set of methods and operators. Read the documentation at
http://docs.python.org/2/library/datetime.html.
Use the datetime module to write a program that gets the current date
and prints the day of the week.
Write a program that takes a birthday as input and prints the user’s
age and the number of days, hours, minutes and seconds until their next
birthday.
For two people born on different days, there is a day when one is twice
as old as the other. That’s their Double Day. Write a program that takes
two birthdays and computes their Double Day.
For a little more challenge, write the more general version that computes
the day when one person is n times older than the other."""

import datetime

def print_date_and_day_of_week():
    date = datetime.date.today()

    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_of_week = days_of_week[date.weekday()]
    print date, " : ", day_of_week



def time_to_next_birthday(birth_year, birth_month, birth_day):
    birth = datetime.datetime(birth_year, birth_month, birth_day)
    current_time = datetime.datetime.now()

    current_age = current_time.year - birth.year - ((current_time.month, current_time.day) < (birth.month, birth.day))

    if (current_time.month, current_time.day) < (birth.month, birth.day):
        next_bday = (current_time.year, birth_month, birth_day)
    else:
        next_bday = (current_time.year + 1, birth_month, birth_day)

    time_to_next_bday = datetime.datetime(*next_bday) - current_time

    print "current age: ", current_age
    print "time to next birthday: ", time_to_next_bday




def find_double_day(bday1, bday2):
    """bday1 is the older person.
    both birthdays are entered as tuples in this format:
    (year, month, day)"""

    person1 = datetime.date(*bday1)
    person2 = datetime.date(*bday2)

    age_diff = -(person1 - person2)

    p1 = int(age_diff.days)
    p2 = 0

    while p2 * 2 != p1:
        p1 += 1
        p2 += 1

    date_at_twice_age = person2 + datetime.timedelta(days=p2)
    print date_at_twice_age, "\n", "person 1 was %d days old, and person 2 was %d days old" % (p1, p2)



def find_n_times_day(bday1, bday2, n):
    """bday1 is the older person.
    both birthdays are entered as tuples in this format:
    (year, month, day)"""

    person1 = datetime.date(*bday1)
    person2 = datetime.date(*bday2)

    age_diff = -(person1 - person2)

    p1 = int(age_diff.days)
    p2 = 0

    while p2 * n != p1:
        if p2 * n > p1:
            print "This never precisely occurred"
            return None
        p1 += 1
        p2 += 1

    date_at_n_times_age = person2 + datetime.timedelta(days=p2)

    print date_at_n_times_age, "\n", "person 1 was %d days old, and person 2 was %d days old" % (p1, p2)


find_double_day((1943, 05, 30), (1994, 05, 16))
find_n_times_day((1991, 05, 30), (1994, 05, 16), 3)

