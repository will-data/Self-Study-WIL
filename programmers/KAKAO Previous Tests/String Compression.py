# Solution by just counting compressed string
def solution(s):
    cutN = 1; answer = len(s)
    while cutN <= len(s)//2:
        length = 0; repeat =1
        for i in range((len(s)//cutN)-1):
            if s[i*cutN:(i+1)*cutN] == s[(i+1)*cutN:(i+2)*cutN]:
                repeat += 1
            elif repeat == 1:
                length += cutN
            else:
                length += (cutN +len(str(repeat))); repeat = 1
        if repeat !=1:
            length += (cutN+len(str(repeat)))
        else:
            length += cutN
        length += len(s)%cutN
        answer = min(answer, length); cutN += 1
    return answer

# Solution by making compressed string
def solution(s):
    cutN = 1; answer = len(s)
    while cutN <= len(s)//2:
        news = ''; repeat =1
        for i in range((len(s)//cutN)-1):
            if s[i*cutN:(i+1)*cutN] == s[(i+1)*cutN:(i+2)*cutN]:
                repeat += 1
            elif repeat == 1:
                news += s[i*cutN:(i+1)*cutN]
            else:
                news += str(repeat) + s[i*cutN:(i+1)*cutN]; repeat = 1
        if repeat !=1:
            news += str(repeat) + s[(len(s)//cutN-1)*cutN:(len(s)//cutN)*cutN]
        else:
            news += s[(len(s)//cutN-1)*cutN:(len(s)//cutN)*cutN]
        news += s[(len(s)//cutN)*cutN:]; cutN +=1
        print(news)
        answer = min(answer,len(news))
    return answer
