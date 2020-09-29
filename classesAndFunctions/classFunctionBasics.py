class Time(object):
    """ Represents the time of day.
    attributes: hour, minutes, second"""

time1 = Time()
time1.hour = 9 
time1.minutes = 59
time1.second = 30

time2 = Time()
time2.hour = 10
time2.minutes = 9
time2.second = 30

def print_time(timeClass):
    print('%0.2d.%0.2d.%0.2d'%(timeClass.hour, timeClass.minutes, timeClass.second))

def add_time(t1, t2):
    sumTime = Time()
    sumTime.hour = t1.hour + t2.hour
    sumTime.minutes = t1.minutes + t2.minutes
    sumTime.second = t1.second + t2.second

    while sumTime.second >= 60 and sumTime.minutes >= 60:
        if sumTime.second >=60:
            sumTime.second -=60
            sumTime.minutes +=1
        if sumTime.minutes >=60:
            sumTime.minutes -=60
            sumTime.hour +=1
        return sumTime
print_time(add_time(time1,time2))
