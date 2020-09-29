import os

cmd = 'cat files/name1.txt'
fp = os.popen(cmd)
print(fp)

fp_read = fp.read()
print(fp_read)
