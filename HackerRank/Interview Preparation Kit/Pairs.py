#!/bin/python3

import math
import os
import random
import re
import sys
s

# My own solution using in and set
# def pairs(k, arr):
#    arr = set(arr); count = 0
#    for i in arr:
#        if (i+k) in arr: count +=1
#        if (i-k) in arr: count +=1
#    return int(count/2)
# Much better solution found in discussions
def pairs(k, arr):
    arr = set(arr);
    return len(arr & set(x + k for x in arr))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
