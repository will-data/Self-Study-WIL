from collections import Counter, OrderedDict
def solution(A, B):
    A_count = Counter(A); B_count = Counter(B);
    A_count = OrderedDict(sorted(A_count.items(),key = lambda i: i[0], reverse = True))
    score = 0; bList = sorted(list(B_count.keys()), reverse=True)
    checkIndex = 0; largeCount = 0
    for a in A_count:
        if checkIndex <= (len(bList)-1):
            while bList[checkIndex] > a:
                largeCount += B_count[bList[checkIndex]]
                checkIndex += 1
                if checkIndex >= (len(bList)-1):
                    break
        score += min(A_count[a], largeCount)
        largeCount = max(0, largeCount - A_count[a])
    return score
