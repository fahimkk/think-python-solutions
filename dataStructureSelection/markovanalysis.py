import string, random, logging
logging.basicConfig(level=logging.DEBUG)

def line_process(line_string):
    line = line_string.lower() 
    word_list = line.split()
    for i in range(len(word_list)):
        word_list[i] = word_list[i].strip(string.punctuation+string.whitespace)
    return word_list
    
def text_process(filename):
    fp = open(filename,'r')
    prefix_dict = {}
    for line in fp:
        word_list = line_process(line)
        for i in range (len(word_list)-2):
            if (word_list[i],word_list[i+1]) in prefix_dict:
                prefix_dict[(word_list[i],word_list[i+1])].append(word_list[i+2])
            else:
                prefix_dict[(word_list[i],word_list[i+1])]= [word_list[i+2]]
    return prefix_dict

            
def markov_analysis(prefix_dict,line_num=8):
    text_list = []
    prefix_list = sorted(prefix_dict.keys())
    prefix1_tup = random.choice(prefix_list)
    current_line = 0
    text_list.extend(list(prefix1_tup))
    while line_num-1 > current_line: 
        if prefix1_tup in prefix_dict: 
            text_list.append(random.choice(prefix_dict[prefix1_tup]))
            prefix1_tup = (text_list[-2],text_list[-1])
        else:
            current_line+=1
            prefix1_tup = random.choice(prefix_list)
            text_list.append('\n')
            text_list.extend(list(prefix1_tup))
    return ' '.join(text_list)


print(markov_analysis(text_process('eric')))


