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

    def print_time(self):
        print('%.2d:%.2d:%.2d'%(self.hour, self.minute, self.second))
    #insead of print_time we can use __str__ method to get string 
    # representation of an object. 
    def __str__(self):
        return '%.2d:%.2d:%.2d'%(self.hour, self.minute, self.second)

    def time_to_int(self):
        return (self.hour * 60 + self.minute) * 60 + self.second

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds) 
    
    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()

start = Time(9,45)

#Time.print_time(start)
#start.print_time()

start.print_time()
print(start)
#end = start.increment(1337)
#end.print_time()

#print(end.is_after(start))
#print(start.is_after(end))

def print_attributes(obj):
    for attr in obj.__dict__:
        print (attr, getattr(obj, attr))

print_attributes(start)
print(start.__dict__)
