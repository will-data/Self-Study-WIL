def solution(N):
    n = 0; current = 1; nex = 1
    while n <N-1:
        current, nex = nex, current+nex
        n +=1
    return 2*(current+nex)
