#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    diffs = [0] * (n+1)
    for a,b,k in queries:
        diffs[a-1] += k
        diffs[b] -= k
    answer = 0; maxA = 0
    for diff in diffs:
        answer += diff; maxA = max(maxA, answer)
    return maxA

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
