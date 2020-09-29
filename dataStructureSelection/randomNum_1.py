""" using cumilative sum list and binary search to get weighted random choice"""

import random

hist = {'a':3,'b':5,'t':9,'k':6,'f':106,'m':49}



def sorted_list(hist):
    sorted_tup_list = sorted(hist.items(), key= lambda x:x[1])
    sorted_key_list = []
    for tup in sorted_tup_list:
        sorted_key_list.append(tup[0])
    return sorted_key_list



def cumilative_list(sorted_list,hist):
    cum_list = []
    i=0
    for index,word in enumerate(sorted_list):
        cum_list.append(hist[word]+i)
        i=cum_list[index]
    return cum_list

def binary_search(num, cumilative_sum_list):
    lower = 0
    higher = len(cumilative_sum_list)-1
    while lower <= higher:
        mid = (lower+higher)//2
        if cumilative_sum_list[mid] < num:
            lower=mid+1
        elif cumilative_sum_list[mid]> num:
            higher = mid-1
        else:
            return mid
    return higher+1 

word_list = sorted_list(hist)
cumilative_sum_list = cumilative_list(word_list,hist)
n = cumilative_sum_list[-1]
rand = random.randint(1,n)  
index = binary_search(rand, cumilative_sum_list)
element = word_list[index]
    
print(rand)
print(word_list)
print(cumilative_sum_list)
print(binary_search(rand,cumilative_sum_list))
print(element)