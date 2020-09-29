import string

def process_line(line_string, hist_dict):
    line = line_string.replace('-',' ')
    for word in line.split():
        word = word.strip(string.punctuation+string.whitespace)
        word = word.lower()
        hist_dict[word] = hist_dict.get(word,0) + 1

def process_file(filename):
    hist = {}
    fp = open(filename,'r')
    for line in fp:
        process_line(line,hist)
    return hist
hist = process_file('hello.txt')
print(hist)
        
def total_words(hist):
    return sum(hist.values())
#print(total_words(hist))

def different_words(hist):
    return len(hist)
#print(different_words(hist))

def most_common(hist):
    t = []
    for key, value in hist.items():
        t.append((value,key))
    t.sort(reverse=True)
    return t
t = most_common(hist)
for freq, word in t[:5]:
    print(word,freq)

def print_most_common(hist, num=10):
    t = most_common(hist)
    print('The most common words are:')
    for freq, word in t[:num]:
        print(word,freq)
#print_most_common(hist,5)

def substrat(d1, d2):
    res = dict()
    for key in d1:
        if key not in d2:
            res[key] = None
    return res

epidemic = process_file('epidemic.txt')
words = process_file('dictionaryLower.txt')
diff = substrat(epidemic,words)
print(len(diff))

set_epidemic = set(epidemic)
set_words = set(words)
set_diff = set_epidemic.difference(set_words)
print(len(set_diff))

