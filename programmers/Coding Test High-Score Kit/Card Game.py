def solution(left, right):
    left = left[::-1];
    right = right[::-1]
    scoreDict = {};
    scoreDict[(0, -1)] = 0

    for i in range(len(right) + 1):
        scoreDict[(0, i)] = 0;
        scoreDict[(i, 0)] = 0

    for i in range(len(left)):
        for j in range(len(right)):
            if left[i] > right[j]:
                scoreDict[(i + 1, j + 1)] = scoreDict[(i + 1, j)] + right[j]
            else:
                scoreDict[(i + 1, j + 1)] = max(scoreDict[(i, j)], scoreDict[(i, j + 1)])

    return scoreDict[(len(left), len(right))]