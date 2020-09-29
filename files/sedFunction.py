import os


def sed(filename_read, filename_write, pattern_string, replacement_string):
    try:
        file_read = open(filename_read,'r')
        line_list = file_read.readlines()
        line_string = ''.join(line_list)
        replaced_string = line_string.replace(pattern_string,replacement_string)
        file_write = open(filename_write,'w')
        file_write.write(replaced_string)
        file_read.close()
        file_write.close()
    except Exception as e:
        print(e,'\nError occured while opening the file')

sed('files/name1.txt','files/nameFahim','Name','Fahim')