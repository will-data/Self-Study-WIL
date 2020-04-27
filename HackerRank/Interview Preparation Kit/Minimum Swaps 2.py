#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    index = [0] * (len(arr) + 1)
    for i, n in enumerate(arr):
        index[n] = i
    swapNum = 0
    for i in range(len(arr)):
        if arr[i] != i + 1:
            swapNum += 1
            arr[index[i + 1]], index[arr[i]] = arr[i], index[i + 1]
    return swapNum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
