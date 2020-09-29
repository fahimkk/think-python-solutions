import os

def file_list(filename,suffix):
    fileList=[]
    for folders,subfolders,filenames in os.walk(os.path.join(os.getcwd(),filename)):
        for filename in filenames:
            if filename.endswith(suffix):
                fileList.append(os.path.join(folders,filename))
    
    return fileList


def check_duplicate(fileList):
    duplicate_dict = {}
    cmd ='md5sum '
    for filename in fileList:
        cmdOutputList = os.popen(cmd+filename).read().split()
        checksum = cmdOutputList[0]
        if checksum in duplicate_dict:
            duplicate_dict[checksum].append(filename)
        else:
            duplicate_dict[checksum] = [filename]
    for key, value in duplicate_dict.copy().items():
        if len(value) < 2:
            del duplicate_dict[key] 

    return duplicate_dict
        
def double_check(dictFile):
    checkList = []
    for filenames in dictFile.values():
        for index in range(1,len(filenames)):
            cmd = f'diff {filenames[0]} {filenames[index]};echo $?' 
            output =os.popen(cmd).read().strip()
            if output =='0':
                continue
            else:
                checkList.append(filenames[index])
    if checkList:
        return checkList
    else:
        return True


fileList = file_list('exp4','.txt')
dupFiles = check_duplicate(fileList)
checkList = double_check(dupFiles)
print(checkList)
