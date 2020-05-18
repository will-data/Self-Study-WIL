def solution(stones, k):
    def checkStones(stones, k):
        zeroCount = 0
        for stone in stones:
            zeroCount = zeroCount + 1 if stone == 0 else 0
            if zeroCount >= k:
                return False
        return True

    def afterStones(stones, m=1):
        return list(max(0, i - m) for i in stones)

    answerMax = 200000000;
    answerMin = 0
    while answerMax - answerMin > 1:
        if checkStones(afterStones(stones, m=((answerMax + answerMin) // 2 - 1)), k):
            answerMin = (answerMax + answerMin) // 2
        else:
            answerMax = (answerMax + answerMin) // 2

    return answerMin