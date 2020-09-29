"""increment, which adds a given number of seconds to a Time object,
Write a “pure” version of increment that creates and returns a new 
Time object rather than modifying the parameter."""

import copy

class Time(object):
    """ Represents the time of day.
    attributes: hour, minutes, second"""

time = Time()
time.hour = 11
time.minute = 59
time.second = 30

def print_time(timeClass):
    print('%0.2d.%0.2d.%0.2d'%(timeClass.hour, timeClass.minute, timeClass.second))

def increment(time, second):
    inc_time = copy.copy(time) 
    inc_time.second = time.second + second
    if inc_time.second >=60:
        div_sec = divmod(inc_time.second, 60)
        inc_time.minute += div_sec[0]
        inc_time.second = div_sec[1]
    if inc_time.minute >=60:
        div_min = divmod(inc_time.minute, 60)
        inc_time.hour += div_min[0]
        inc_time.minute = div_min[1]
    return inc_time
print_time(time)
newTime = increment(time, 125)
print_time(newTime)
print_time(time)