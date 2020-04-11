import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    plus = sum(x > 0 for x in arr)
    minus = sum(x < 0 for x in arr)
    zero = sum(x == 0 for x in arr)

    print(round(plus / n, 6))
    print(round(minus / n, 6))
    print(round(zero / n, 6))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
