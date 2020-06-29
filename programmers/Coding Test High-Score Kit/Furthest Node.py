def solution(n, edges):
    # First, make adjacent matrix for the graph
    adjGra = {}
    for edge in edges:
        adjGra[edge[0]] = [edge[1]] if edge[0] not in adjGra else adjGra[edge[0]] + [edge[1]]
        adjGra[edge[1]] = [edge[0]] if edge[1] not in adjGra else adjGra[edge[1]] + [edge[0]]
    for node in range(1, (n + 1)):
        if node not in adjGra:
            adjGra[node] = []

    # Next, check the distance from 1
    visitedNodes = set([1])
    distDict = {0: set([1])};
    dist = 0
    while visitedNodes != set(list(range(1, (n + 1)))):
        nextSet = set()
        for i in distDict[dist]:
            nextSet.update(adjGra[i])
        distDict[(dist + 1)] = nextSet - visitedNodes
        visitedNodes.update(nextSet)
        dist += 1

    return len(distDict[max(distDict)])