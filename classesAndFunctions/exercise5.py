"""Rewrite increment using time_to_int and int_to_time."""

class Time(object):
    """ Represents the time of day.
    attributes: hour, minutes, second"""

time1 = Time()
time1.hour = 9 
time1.minute = 59
time1.second = 30

time2 = Time()
time2.hour = 10
time2.minute = 9
time2.second = 30

def print_time(timeClass):
    print('%0.2d.%0.2d.%0.2d'%(timeClass.hour, timeClass.minute, timeClass.second))

def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds,60)
    time.hour, time.minute = divmod(minutes,60)
    return time

def add_time(t1, t2):
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)

def increment (time, seconds):
    seconds = seconds+time_to_int(time)
    return int_to_time(seconds)

print_time(time1)
print_time(time2)
print_time(add_time(time1,time2))
print_time(increment(time1, 125))

