#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    if len(arr) == 1: return (max(0, arr[0]))
    maxSubset = {}
    maxSubset[0] = max(0, arr[0])
    maxSubset[1] = max(arr[0], arr[1], 0)
    if len(arr) == 2: return maxSubset[1]
    for i in range(2, len(arr)):
        maxSubset[i] = max(maxSubset[i - 1], maxSubset[i - 2] + arr[i])
    return maxSubset[len(arr) - 1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
