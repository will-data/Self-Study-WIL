#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stepPerms function below.
stairMethod = {1:1, 2:2, 3:4}


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())
    n = []; res = []

    for s_itr in range(s):
        n.append(int(input()))
    if max(n) > 3:
        for i in range(3,max(n)):
            stairMethod[i+1] = (stairMethod[i] + stairMethod[i-1] + stairMethod[i-2]) % (10**10+7)

    for s_itr in range(s):
        res = stairMethod[n[s_itr]]

        fptr.write(str(res) + '\n')

    fptr.close()
