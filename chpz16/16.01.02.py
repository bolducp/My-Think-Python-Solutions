"""Write a boolean function called is_after that takes two Time objects,
t1 and t2, and returns True if t1 follows t2 chronologically and False
otherwise. Challenge: don’t use an if statement."""


class Time(object):
    """Represents the time of day.
    attributes: hour, minute, second"""

time = Time()
time.hour = 11
time.minute = 59
time.second = 30

time2 = Time()
time2.hour = 11
time2.minute = 59
time2.second = 35

def is_after(t1, t2):
    return (t1.hour, t1.minute, t1.second) > (t2.hour, t2.minute, t2.second)

