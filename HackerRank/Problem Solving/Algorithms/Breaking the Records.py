#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the breakingRecords function below.
def breakingRecords(scores):
    minScore = scores[0];
    maxScore = scores[0]
    minCnt = 0;
    maxCnt = 0
    if len(scores) == 1:
        pass
    else:
        for i in scores[1:]:
            if i > maxScore:
                maxScore = i
                maxCnt += 1
            if i < minScore:
                minScore = i
                minCnt += 1
    return ([maxCnt, minCnt])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
