"""Write a __cmp__ method for Time objects. Hint: you can use tuple
comparison, but you also might consider using integer subtraction."""


class Time(object):
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return "%.2d:%.2d:%.2d" % (self.hour, self.minute, self.second)

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds


    def __cmp__(self, other):
        time1 = self.hour, self.minute, self.second
        time2 = other.hour, other.minute, other.second
        return cmp(time1, time2)

#Alternatively:
    def cmp2(self, other):
        return cmp(self.time_to_int(), other.time_to_int())


def int_to_time(seconds):
    minutes, second = divmod(seconds, 60)
    hour, minute = divmod(minutes, 60)
    time = Time(hour, minute, second)
    return time


t = Time(11, 54, 12)
t2 = Time(11, 54, 10)


print t.__cmp__(t2)
print t.cmp2(t2)
