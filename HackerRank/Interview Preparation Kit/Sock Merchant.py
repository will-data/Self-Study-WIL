#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    color_count = Counter(ar)
    return sum(color_count[color]//2 for color in color_count)

if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
    print(result)
#    fptr.write(str(result) + '\n')

#    fptr.close()
