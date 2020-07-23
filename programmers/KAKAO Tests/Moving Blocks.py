def solution(board):
    l = len(board)
    padBoard = [[1 for x in range(l + 2)] for y in range(l + 2)]
    for i in range(l):
        for j in range(l):
            padBoard[1 + i][1 + j] = board[i][j]

    robotLocs = set({(1, 1, 0)})  # [x,y,direction]; direction = 0(right), 1(down)

    def moveRobot(robotLoc):
        x, y, direction = robotLoc
        nextLoc = set()
        for m in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            if direction == 0:
                if padBoard[x + m[0]][y + m[1]] == 0 and padBoard[x + m[0]][y + 1 + m[1]] == 0:
                    nextLoc.add((x + m[0], y + m[1], 0))
            else:
                if padBoard[x + m[0]][y + m[1]] == 0 and padBoard[x + 1 + m[0]][y + m[1]] == 0:
                    nextLoc.add((x + m[0], y + m[1], 1))
        return nextLoc

    def rotateRobot(robotLoc):
        x, y, direction = robotLoc
        nextLoc = set()
        if direction == 0:
            if padBoard[x + 1][y] == 0 and padBoard[x + 1][y + 1] == 0:
                nextLoc.add((x, y + 1, 1))
                nextLoc.add((x, y, 1))
            if padBoard[x - 1][y] == 0 and padBoard[x - 1][y + 1] == 0:
                nextLoc.add((x - 1, y, 1))
                nextLoc.add((x - 1, y + 1, 1))
        if direction == 1:
            if padBoard[x][y + 1] == 0 and padBoard[x + 1][y + 1] == 0:
                nextLoc.add((x, y, 0))
                nextLoc.add((x + 1, y, 0))
            if padBoard[x][y - 1] == 0 and padBoard[x + 1][y - 1] == 0:
                nextLoc.add((x + 1, y - 1, 0))
                nextLoc.add((x, y - 1, 0))
        return nextLoc

    target = set({(l, l - 1, 0), (l - 1, l, 1)})
    moveCnt = 0;
    visited = set({(1, 1, 0)})
    while True:
        moveCnt += 1;
        nextLoc = set()
        for robotLoc in robotLocs:
            nextLoc.update(moveRobot(robotLoc) - visited)
            nextLoc.update(rotateRobot(robotLoc) - visited)
        if nextLoc & target:
            return moveCnt
        else:
            robotLocs = nextLoc
            visited.update(nextLoc)



