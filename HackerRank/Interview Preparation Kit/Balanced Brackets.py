#!/bin/python3

import math
import os
import random
import re
import sys

# My original Solution
def isBalanced(s):
    stackBrac = []; checkDict = {'(':')','{':'}','[':']'}
    for item in s:
        if item in ['(','{','[']:
            stackBrac.append(item)
        elif stackBrac:
            checkBrac = stackBrac.pop()
            if checkDict[checkBrac] != item:
                return 'NO'
        else:
            return 'NO'
    return 'YES' if not stackBrac else 'NO'

# Interesting solution in discussions, without using stack
#def isBalance(s):
#    n= -1
#    while len(s) != n:
#        n = len(s)
#        s = s.replace('()','')
#        s = s.replace('{}','')
#        s = s.replace('[]','')
#    return 'YES' if len(s) == 0 else 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
