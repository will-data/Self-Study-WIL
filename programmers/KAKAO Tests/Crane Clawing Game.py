def solution(board, moves):
    # At first, make stack of each columns
    boardStack = [[] for _ in range(len(board[0]))]
    for row in board[::-1]:
        # Watch out, column index is subtracted by -1
        for column, element in enumerate(row):
            if element != 0:
                boardStack[column].append(element)
    bucketStack = [];
    exploded = 0;
    for move in moves:
        if boardStack[(move - 1)]:
            pick = boardStack[(move - 1)].pop()
            if bucketStack:
                if bucketStack[-1] == pick:
                    bucketStack.pop()
                    exploded += 2
                else:
                    bucketStack.append(pick)
            else:
                bucketStack.append(pick)

    return exploded