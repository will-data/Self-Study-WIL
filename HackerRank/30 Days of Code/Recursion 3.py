#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the factorial function below.
# def factorial(n):
#     return(1 if n==1 else n*factorial(n-1))
# Another solution with using lambda
factorial = lambda x : 1 if x<=1 else x*factorial(x-1)

if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    print(factorial(n))

#    fptr.write(str(result) + '\n')

#    fptr.close()
