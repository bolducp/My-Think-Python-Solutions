"""increment, which adds a given number of seconds to a Time object, can
be written naturally as a modifier. Here is a rough draft:

def increment(time, seconds):
    time.second += seconds

    if time.second >= 60:
        time.second -= 60
        time.minute += 1

    if time.minute >= 60:
        time.minute -= 60
        time.hour += 1
The first line performs the basic operation; the remainder deals with
the special cases we saw before.
Is this function correct? What happens if the parameter seconds is much
greater than sixty?

In that case, it is not enough to carry once; we have to keep doing it
until time.second is less than sixty. One solution is to replace the
if statements with while statements. That would make the function correct,
but not very efficient.

Exercise 3
Write a correct version of increment that doesn’t contain any loops."""

class Time(object):
    """Represents the time of day.
    attributes: hour, minute, second"""

time = Time()
time.hour = 11
time.minute = 59
time.second = 30



def increment(time, seconds):
    time.second += seconds

    add_mins, remain_seconds = divmod(time.second, 60)

    time.minute += add_mins
    time.second = remain_seconds

    add_hours, remain_minute = divmod(time.minute, 60)

    time.hour += add_hours
    time.minute = remain_minute

