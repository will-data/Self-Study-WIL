import math
import os
import random
import re
import sys

# Complete the aVeryBigSum function below.
## Actually, Python3 doesn't need any code to solve this problem..
def aVeryBigSum(ar):
    return sum(i for i in ar)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
