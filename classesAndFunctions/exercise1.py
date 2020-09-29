"""Write a function called print_time that takes a Time object and prints 
it in the form hour:minute:second. Hint: the format sequence '%.2d' prints 
an integer using at least two digits, including a leading zero if necessary."""

class Time(object):
    """ Represents the time of day.
    attributes: hour, minutes, second"""

time = Time()
time.hour = 11
time.minutes = 59
time.second = 30

def print_time(timeClass):
    print('%0.2d.%0.2d.%0.2d'%(timeClass.hour, timeClass.minutes, timeClass.second))

print_time(time)
