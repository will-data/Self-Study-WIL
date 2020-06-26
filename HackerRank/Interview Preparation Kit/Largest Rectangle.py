#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the largestRectangle function below.
def largestRectangle(h):
    hStack = []
    h.append(0)
    maxVal = 0
    for i in range(len(h)):
        leftIndex = i
        while hStack and hStack[-1][0] >= h[i]:
            last = hStack.pop()
            leftIndex = last[1]
            maxVal = max(maxVal, last[0]*(i-leftIndex))
        maxVal = max(maxVal, h[i]*(i+1-leftIndex))
        hStack.append((h[i],leftIndex))
    return maxVal


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
