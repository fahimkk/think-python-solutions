import string

f = open('dictionary.txt','r')
word_list = f.read().split()
for i in range(len(word_list)):
    word_list[i] = word_list[i].lower()

word_string = '\n'.join(word_list)
g = open('dictionaryLower.txt','w')
g.write(word_string)
f.close()
g.close()
