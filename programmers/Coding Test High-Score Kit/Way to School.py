def solution(m, n, puddles):
    route = [[0 for x in range(n)] for y in range(m)]
    avaM = m;
    avaN = n;
    for x, y in puddles:
        if x == 1:
            avaN = min(avaN, y - 1)
        if y == 1:
            avaM = min(avaM, x - 1)
    for j in range(avaN):
        route[0][j] = 1
    for i in range(avaM):
        route[i][0] = 1

    for i in range(1, m):
        for j in range(1, n):
            if [i + 1, j + 1] not in puddles:
                route[i][j] = (route[i - 1][j] + route[i][j - 1]) % 1000000007

    return route[-1][-1]