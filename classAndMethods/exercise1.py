"""Rewrite time_to_int (from Section 16.4) as a method. It is probably not appropriate 
to rewrite int_to_time as a method; what object you would invoke it on?"""

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds,60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

class Time(object):
    def print_time(self):
        print('%.2d:%.2d:%.2d'%(self.hour, self.minute, self.second))
    
    def time_to_int(self):
        return (self.hour * 60 + self.minute) * 60 + self.second

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds) 
    

start = Time()
start.hour = 9
start.minute = 45
start.second = 00

start.print_time()
end = start.increment(1337)
end.print_time()
