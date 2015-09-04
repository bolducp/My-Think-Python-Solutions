"""Write a function called mul_time that takes a Time object and a
number and returns a new Time object that contains the product of
the original Time and the number.
Then use mul_time to write a function that takes a Time object that
represents the finishing time in a race, and a number that represents
the distance, and returns a Time object that represents the average
pace (time per mile)."""


class Time(object):
    """Represents the time of day.
    attributes: hour, minute, second"""

time = Time()
time.hour = 1
time.minute = 59
time.second = 30

time2 = Time()
time2.hour = 11
time2.minute = 59
time2.second = 35

def print_time(time):
    print "%.2d:%.2d:%.2d" % (time.hour, time.minute, time.second)


def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


def mul_time(time, num):
    new_time = int_to_time((time_to_int(time)) * num)
    return new_time


def div_time(time, num):
    new_time = int_to_time((time_to_int(time)) / float(num))
    return new_time


def find_average_pace(time, distance):
    time_per_mile = div_time(time, distance)
    print_time(time_per_mile)
    return time_per_mile

#Alternatively:

def find_average_pace2(time, distance):
    time_per_mile = mul_time(time, (1.0 / distance))
    print_time(time_per_mile)
    return time_per_mile

find_average_pace(time, 2)
find_average_pace2(time, 2)








