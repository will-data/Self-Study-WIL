def solution(n, results):
    winDict = {};
    loseDict = {}
    for i in range(1, (n + 1)):
        winDict[i] = set();
        loseDict[i] = set()
    # First, update the win/lose set with results
    for win, lose in results:
        winDict[win].add(lose)
        loseDict[lose].add(win)

    # Next, update the set with applying the following logic; If A beated B and B beated C, A will beat C
    for i in range(1, (n + 1)):
        for loser in winDict[i]:
            for winner in loseDict[i]:
                winDict[winner].add(loser)
                loseDict[loser].add(winner)

    answer = 0
    for i in range(1, (n + 1)):
        if len(winDict[i]) + len(loseDict[i]) == n - 1:
            answer += 1
    return answer