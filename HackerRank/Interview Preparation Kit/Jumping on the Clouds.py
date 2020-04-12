#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    index = 0; jump_cnt = 0;
    while index < len(c)-3:
        index += 1+(c[index+2] ==0)*1
        jump_cnt += 1
    return(jump_cnt+1)


if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c)
    print(result)
#    fptr.write(str(result) + '\n')
#    fptr.close()
