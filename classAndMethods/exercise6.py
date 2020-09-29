"""Change the attributes of Time to be a single integer representing seconds since midnight.
 Then modify the methods (and the function int_to_time) to work with the new implementation. 
 You should not have to modify the test code in main. When you are done, the output should be the same as before."""
class Time(object):
    def __init__(self,second=0):
        self.second = second

    def __str__(self):
        return '%d'%(self.second)

    def increment(self, seconds):
        return Time(seconds + self.second)
     
    def is_after(self, other):
        return self.second > other.second

    
    def __add__(self, other):
        if isinstance(other,Time):
            return (self.second + other.second)
        else:
            return self.increment(other)

    def __radd__(self,other):
        return self.__add__(other)

start = Time(945)
duration = Time(55)


print(start)
print(68+start)
print(start+89)
print(start+duration)
print(start.is_after(duration))