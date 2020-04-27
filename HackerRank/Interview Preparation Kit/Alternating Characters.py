#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import groupby

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    count_dups = [sum(1 for _ in group) for _, group in groupby(s)]
# To understand how itertoos.groupby works for this example, check an exmaple below
#print([[k,list(g)] for k,g in groupby('AAAAbBBCCDAABBB')])
    return sum(a-1 for a in count_dups)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
