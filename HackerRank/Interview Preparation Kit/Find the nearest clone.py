#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque


def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    # First, make adjacent matrix for the graph
    adjGra = {}
    for i_from, i_to in zip(graph_from, graph_to):
        adjGra[i_from] = [i_to] if i_from not in adjGra else adjGra[i_from] + [i_to]
        adjGra[i_to] = [i_from] if i_to not in adjGra else adjGra[i_to] + [i_from]
    for numNode in range(1, (graph_nodes + 1)):
        if numNode not in adjGra:
            adjGra[numNode] = []

    # Next, check index of node with color val
    valIndex = set()
    for i, color in enumerate(ids):
        if color == val:
            valIndex.add(i + 1)

    # Then, Find the nearest route by checking one-by-one using BFS
    minDists = []
    for startN in valIndex:
        visitedN = set([startN]);
        currentSet = set([startN]);
        dist = 0
        while dist < (graph_nodes - 1):
            nextSet = set()
            for i in currentSet:
                nextSet.update(adjGra[i])
            if nextSet & (valIndex - set([startN])):
                dist += 1;
                break
            else:
                currentSet = nextSet - visitedN
                visitedN.update(nextSet)
                dist += 1

        if dist < (graph_nodes - 1): minDists.append(dist)

    if not minDists:
        return -1
    else:
        return min(minDists)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    graph_nodes, graph_edges = map(int, input().split())

    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges

    for i in range(graph_edges):
        graph_from[i], graph_to[i] = map(int, input().split())

    ids = list(map(int, input().rstrip().split()))

    val = int(input())

    ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)

    fptr.write(str(ans) + '\n')

    fptr.close()
