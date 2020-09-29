#word frequency analysis
""" write a program that reads a file, breaks each line inot words,strips 
whitespace and punnctuation from the words, and converts them to lowercase."""

import string

f = open('hello.txt','r')
line_list = f.readlines()
print(line_list)
word_list=[]
for line in line_list:
    words = line.split() 
    word_list.extend(words)
print(word_list)

for i in range(len(word_list)):
    word_list[i]= word_list[i].strip(string.punctuation).lower()
print(word_list)

f.close()
