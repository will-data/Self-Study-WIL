#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the isValid function below.
def isValid(s):
    charCnt = Counter(s).values()
    charCntCnt = Counter(charCnt)
    diff = lambda x: abs(list(x)[0]-list(x)[1])
    if len(charCntCnt) == 1:
        return 'YES'
    elif len(charCntCnt) == 2:
        if diff(charCntCnt.keys()) == 1 and 1 in charCntCnt.values():
            return 'YES'
        elif 1 in charCntCnt:
            if charCntCnt[1] == 1:
                return 'YES'

    return 'NO'





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
