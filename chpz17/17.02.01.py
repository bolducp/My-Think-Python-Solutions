"""Rewrite time_to_int (from Section 16.4) as a method. It is probably
not appropriate to rewrite int_to_time as a method; what object you
would invoke it on?"""

class Time(object):
    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

t = Time()
t.hour = 11
t.minute = 59
t.second = 30

print t.time_to_int()