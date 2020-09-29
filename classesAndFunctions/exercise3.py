"""increment, which adds a given number of seconds to a Time object,
Write a correct version of increment that doesn’t contain any loops."""


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
    time.second +=second
    if time.second >=60:
        div_sec = divmod(time.second, 60)
        time.minute += div_sec[0]
        time.second = div_sec[1]
    if time.minute >=60:
        div_min = divmod(time.minute, 60)
        time.hour += div_min[0]
        time.minute = div_min[1]

print_time(time)
increment(time, 125)
print_time(time)