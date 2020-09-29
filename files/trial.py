import urllib.request

url = urllib.request.urlopen('http://www.uszip.com/zip/02492')
text = url.read()
print(text)