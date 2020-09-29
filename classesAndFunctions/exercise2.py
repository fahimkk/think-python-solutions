"""Write a boolean function called is_after that takes two Time objects, t1 and t2, and returns 
True if t1 follows t2 chronologically and False otherwise. Challenge: don’t use an if statement."""

class Time(object):
    """ Represents the time of day.
    attributes: hour, minutes, second"""

time1 = Time()
time1.hour = 11 
time1.minutes = 59
time1.second = 30

time2 = Time()
time2.hour = 10
time2.minutes = 9
time2.second = 30



def is_after(t1, t2):
    t1_sec = t1.hour*60*60+t1.minutes*60+t1.second
    t2_sec = t2.hour*60*60+t2.minutes*60+t2.second
    return t1_sec > t2_sec
    #return {True:True,False:False} [t1.hour > t2.hour ]

print(is_after(time1,time2))
#print((False,True)[time1.hour >= time2.hour]) # Use tuple for selecting an item  (if_test_false,if_test_true)[test] 
#print({True:True,False:False}[time1.hour >= time2.hour])
