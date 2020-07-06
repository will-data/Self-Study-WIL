#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the freqQuery function below.
def freqQuery(queries):
    freqDict = {};
    answer = []
    for query in queries:
        if query[0] == 1:
            if query[1] not in freqDict:
                freqDict[query[1]] = 1
            else:
                freqDict[query[1]] += 1
        elif query[0] == 2:
            if query[1] in freqDict:
                if freqDict[query[1]] == 1:
                    del freqDict[query[1]]
                else:
                    freqDict[query[1]] -= 1
        else:
            if query[1] in set(freqDict.values()):
                answer.append(1)
            else:
                answer.append(0)
    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
