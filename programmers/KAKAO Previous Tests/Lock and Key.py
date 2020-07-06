def solution(key, lock):
    n = len(lock);
    m = len(key)

    def rotateKey(key, rotate):
        while rotate != 0:
            newKey = [[0 for x in range(m)] for y in range(m)]
            for i, row in enumerate(key):
                for j, value in enumerate(row):
                    newKey[j][m - 1 - i] = value
            key = newKey;
            rotate -= 1
        return key

    for rotate in range(4):
        keyMat = rotateKey(key, rotate)
        for startX in range(n + m - 1):
            for startY in range(n + m - 1):
                checkMat = [[0 for x in range(n + 2 * m - 2)] for y in range(n + 2 * m - 2)]
                for i in range(m):
                    for j in range(m):
                        checkMat[startX + i][startY + j] = keyMat[i][j]

                unLock = True
                for i in range(n):
                    for j in range(n):
                        if unLock:
                            # print(checkMat[m+i-1][m+j-1], lock[i][j])
                            if checkMat[m + i - 1][m + j - 1] + lock[i][j] != 1:
                                unLock = False
                if unLock:
                    return True
    return False