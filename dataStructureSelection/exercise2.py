#word frequency analysis
""" write a program that reads a file, breaks each line inot words,strips 
whitespace and punnctuation from the words, and converts them to lowercase."""

import string

def book_dict(book_name):
    book_file = open(book_name,'r')
    book_line_list = book_file.readlines()[75:]
    word_dict = {}
    for line in book_line_list:
        line_replaced = line.replace('-',' ')
        word_list = line_replaced.split()
        for word in word_list:
            striped_word = word.strip(string.punctuation+string.whitespace+'0123456789').lower()
            if striped_word in word_dict:
                word_dict[striped_word]+=1
            else:
                word_dict[striped_word] = 1
    book_file.close()
    return word_dict
print(book_dict('epidemic.txt'))

def most_vocabs(book1,book2):
    book1_dict = book_dict(book1) 
    book2_dict = book_dict(book2)
    if len(book1_dict) > len(book2_dict):
        print(f"{book1} has extensive vocabulary")
    else:
        print(f"{book2} has extensive vocabulary")

most_vocabs('epidemic.txt','historia.txt')

def frequent_word(book, top=20):
    bookdict_file = book_dict(book)
    sorted_dict_tuple = sorted(bookdict_file.items(), key= lambda x:x[1], reverse=True )
    for tup in sorted_dict_tuple[:top]:
        print(tup[0])
    
frequent_word('epidemic.txt',3)

def check_words(book, dictionary):
    dict_open = open(dictionary,'r')
    dict_word_list = dict_open.read().split()
    bookdict_file = book_dict(book)
    bookword_list = sorted(bookdict_file.keys())
    num_words_not_in_dictionary = 0
    for word in bookword_list:
        if word not in dict_word_list:
            num_words_not_in_dictionary+=1
    return print(f'words in {book}: {len(bookdict_file)}\nwords in {dictionary}: {len(dict_word_list)}\nWORDS DIFFERENT {num_words_not_in_dictionary}')

check_words('epidemic.txt','dictionaryLower.txt')