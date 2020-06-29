def solution(triangle):
    if len(triangle) == 1: return triangle[0][0]

    depth = 2;
    dist = [triangle[0][0]]
    while depth <= len(triangle):
        newDist = [0] * depth
        newDist[0] = dist[0] + triangle[depth - 1][0]
        newDist[-1] = dist[-1] + triangle[depth - 1][-1]
        for i in range(1, (depth - 1)):
            newDist[i] = max(dist[i - 1], dist[i]) + triangle[depth - 1][i]
        dist = newDist;
        depth += 1
    return max(newDist)