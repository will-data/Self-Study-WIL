#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the triplets function below.
def triplets(A, B, C):
    A = sorted(list(set(A)))
    B = sorted(list(set(B)))
    C = sorted(list(set(C)))

    answer = 0
    ai, bi, ci = 0, 0, 0
    while bi < len(B):
        while ai < len(A) and A[ai] <= B[bi]:
            ai += 1
        while ci < len(C) and C[ci] <= B[bi]:
            ci += 1
        answer += ai * ci
        bi += 1

    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()
