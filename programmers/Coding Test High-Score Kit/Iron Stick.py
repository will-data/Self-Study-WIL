def solution(arrangement):
    stickCount = 0; cutCount = 0
    answer = 0; i = 0
    while i < len(arrangement)-1:
        if arrangement[i] == '(' and arrangement[i+1] == ')':
            answer += cutCount
            i += 2
        else:
            stickCount += 1
            cutCount += (1 if arrangement[i] == '(' else -1)
            i += 1
    return answer + (stickCount+1)/2