import string
msg = 'TOBEORNOTTOBEORTOBEORNOT';

def lzwComp(msg):
    myDict = dict(zip(string.ascii_uppercase, range(1,27)))
    zipIndex = []; indexNum = 27; i=0;
    while i < len(msg):
        j=1
        while ((i+j)<=len(msg)) and(msg[i:(i+j)] in myDict):
            j+=1
        zipIndex.append(myDict[msg[i:(i+j-1)]])
        myDict[msg[i:(i+j)]] = indexNum
        indexNum += 1
        i += j-1
    return zipIndex
print(lzwComp(msg))