def solution(clothes):
    cloDict = dict()
    for cloname, cloType in clothes:
        if cloType in cloDict:
            cloDict[cloType] += 1
        else:
            cloDict[cloType] = 1
    answer = 1
    for cloType in cloDict:
        answer = answer * (cloDict[cloType]+1)
    return answer -1