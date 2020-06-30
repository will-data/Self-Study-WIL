#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the flippingBits function below.
def flippingBits(n):
    check32 = [0] * 32
    i = 1
    while n > 0:
        check32[-i] = n % 2
        n = n // 2;
        i += 1

    return sum([(2 ** (i - 1)) * (1 - check32[-i]) for i in range(1, 33)])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
