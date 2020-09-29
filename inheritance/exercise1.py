"""Write a __cmp__ method for Time objects. Hint: you can use tuple 
comparison, but you also might consider using integer subtraction."""

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
    
    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()

    def __lt__(self, other):
        return self.time_to_int() < other.time_to_int()
    def __eq__(self, other):
        return self.time_to_int() == other.time_to_int()


start = Time(9,10)
end = Time(10,10)
print(start.is_after(end))
print(end.is_after(start))
print(start==end)