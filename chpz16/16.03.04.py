"""Write a “pure” version of increment that creates and returns a new
Time object rather than modifying the parameter."""


class Time(object):
    """Represents the time of day.
    attributes: hour, minute, second"""

time = Time()
time.hour = 11
time.minute = 59
time.second = 30


def print_time(time):
    print "%.2d:%.2d:%.2d" % (time.hour, time.minute, time.second)


def increment(time, seconds):
    new_time = Time()
    new_time.second = time.second + seconds

    add_mins, remain_seconds = divmod(new_time.second, 60)
    new_time.minute = time.minute + add_mins
    new_time.second = remain_seconds

    add_hours, remain_minute = divmod(new_time.minute, 60)
    new_time.hour = time.hour + add_hours
    new_time.minute = remain_minute

    return new_time
