#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(Q):
    bribeNums = 0
    for i, q in enumerate(Q):
        if (q-i-1) > 2:
            print('Too chaotic'); return
        for j in range(max(q-2,0),i):
            if Q[j] > q: bribeNums += 1

    print(bribeNums)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
