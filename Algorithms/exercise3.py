"""Write a function called bisection that takes a sorted list and a target value and 
returns the index of the value in the list, if it’s there, or None if it’s not.
Or you could read the documentation of the bisect module and use that!"""

import bisect

data = [12,23,56,58,78,89,96]

def bisection(arr, target):
    low=0
    high = len(arr)-1

    while low <= high:
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid-1
        else:
            low = mid+1

print(bisection(data, 56))

def bisection_recursive(arr, target, low, high):
    if low > high:
        return None 
    else:
        mid = (low+high)//2
        if arr[mid] ==target :
            return mid
        elif arr[mid] < target :
            return bisection_recursive(arr, target, mid+1, high)
        else:
            return bisection_recursive(arr, target, low, mid-1)
            
print(bisection_recursive(data, 56, 0, len(data)-1))
 
print('left bisect position:', bisect.bisect_left(data, 56))
print('normal bisect position:', bisect.bisect(data, 56))
print('right bisect position:', bisect.bisect_right(data, 56))
bisect.insort(data,56)
print(data)