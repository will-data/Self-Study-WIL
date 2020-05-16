def solution(n):
    if n == 1: return 1
    if n == 2: return 2
    else:
        prev, current = 1,2
        i = 2
        while i != n:
            prev, current = current%1000000007, (prev + current)%1000000007
            i += 1
        return current