#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the countTriplets function below.
def countTriplets(arr, r):
    triCnt = 0
    midCnt = defaultdict(int); lastCnt = defaultdict(int)
    for i in arr:
        # Check if i can be last triplet. If it is, add cnt
        triCnt += lastCnt[i]
        # Check if i can be middle triplet. Add cnt to that case
        lastCnt[i*r] += midCnt[i]
        # Check if i can be first triplet. Add cnt to that case
        midCnt[i*r] += 1
    return triCnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
