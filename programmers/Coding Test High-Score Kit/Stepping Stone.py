def solution(distance, rocks, n):
    rocks.sort(); rocks.append(distance)
    left, right = 0, distance
    while left <= right:
        mid = (left + right) // 2
        removeCnt = 0; current = 0; dist = distance
        for i in range(len(rocks)):
            if rocks[i] - current < mid:
                removeCnt += 1
            else:
                dist = min(rocks[i]-current,dist)
                current = rocks[i]
        if removeCnt > n:
            right = mid -1
        else:
            left = mid +1
    return right