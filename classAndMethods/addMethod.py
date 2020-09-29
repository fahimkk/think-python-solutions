def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds,60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

class Time(object):
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '%.2d:%.2d:%.2d'%(self.hour, self.minute, self.second)

    def time_to_int(self):
        return (self.hour * 60 + self.minute) * 60 + self.second

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds) 
    
    def __add__(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)
    
start = Time(9,45)
print(start)

duration = Time(1,35)
print(start+duration)   #this is because of method __add__

