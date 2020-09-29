""" Write a function named choose_from_hist that takes a histogram_dict and returns 
a random value from the histogram, chosen with probability in proportion to frequency. """

import random

def histogram_dict(data_list):
    hist_dict = {}
    for word in data_list:
        if word not in hist_dict:
            hist_dict[word] = 1
        else:
            hist_dict[word]+=1
    return hist_dict

t = ['a','b','b','a','g','z','a','f','a','k']

def choose_from_hist(data_dict):
    total_value = 0
    for value in data_dict.values():
        total_value= total_value+value
    random_key = random.choice(sorted(data_dict))
    return f'{random_key} : with probability {data_dict[random_key]}/{total_value}'
print(choose_from_hist(histogram_dict(t)))


def choose_from_hist_frequency(data_dict):
    total_value = 0
    for value in data_dict.values():
        total_value= total_value+value
    random_key = random.choices(sorted(data_dict.items(), key= lambda x:x[1], reverse=True), weights= sorted(data_dict.values(),reverse=True))
    return f'{random_key[0][0]} : with probability {random_key[0][1]}/{total_value}'
print(choose_from_hist_frequency(histogram_dict(t)))

def random_word (data_dict):
    t = []
    for key, value in data_dict.items():
        t.extend(key * value)
    return random.choice(t)

print(random_word(histogram_dict(t)))