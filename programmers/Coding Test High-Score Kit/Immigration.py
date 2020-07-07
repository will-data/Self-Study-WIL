def solution(n, times):
    leftLim = 1; rightLim = max(times) * n; answer = max(times) * n
    while leftLim <= rightLim:
       # print(leftLim, rightLim)
        lim = (leftLim + rightLim)//2; check = sum([lim//time for time in times])
        if check >= n:
            answer = min(answer, lim)
            rightLim = lim - 1
        elif check < n:
            leftLim = lim + 1
    return answer