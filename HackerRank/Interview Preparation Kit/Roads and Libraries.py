#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict


# Complete the roadsAndLibraries function below.
def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_lib <= c_road:
        return n * c_lib
    else:
        # First, make adjacent matrix for the graph
        adjCities = {}
        for con in cities:
            adjCities[con[0]] = [con[1]] if con[0] not in adjCities else adjCities[con[0]] + [con[1]]
            adjCities[con[1]] = [con[0]] if con[1] not in adjCities else adjCities[con[1]] + [con[0]]
        for city in range(1, n + 1):
            if city not in adjCities:
                adjCities[city] = []
        # Check the number of connected city groups
        visitedCities = set()
        connectedGroupCnt = 0
        for checkCity in range(1, n + 1):
            if checkCity not in visitedCities:
                connectedGroupCnt += 1
                checkStack = [checkCity]
                while checkStack:
                    visitCity = checkStack.pop()
                    if visitCity not in visitedCities:
                        visitedCities.add(visitCity)
                        checkStack += adjCities[visitCity]
        # If there are p connectedGroup, we need to build p libraries and repair n-p roads
        return (connectedGroupCnt * c_lib + (n - connectedGroupCnt) * c_road)


# You should be careful to not exceed time limit in this question.
## DO NOT USE 'in' method to list, because it is O(N**2) algorithm. Instad, use 'in' method to set, because it is O(N) algorithm.


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nmC_libC_road = input().split()
        n = int(nmC_libC_road[0])
        m = int(nmC_libC_road[1])
        c_lib = int(nmC_libC_road[2])
        c_road = int(nmC_libC_road[3])

        cities = []
        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
