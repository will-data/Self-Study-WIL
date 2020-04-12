#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    altitude = 0; valley_count = 0
    for step in s:
        if altitude == 0 and step == 'D':
            valley_count += 1
        altitude += (step == 'U')*2-1
    return valley_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
