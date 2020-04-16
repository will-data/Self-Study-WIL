#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    n = len(arr); m = len(arr[0])
    maxSum = -9*7
    for i in range(n-2):
        for j in range(m-2):
            hgSum = sum(arr[i][j:j+3]+[arr[i+1][j+1]]+arr[i+2][j:j+3])
            if maxSum < hgSum: maxSum = hgSum
    return maxSum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
