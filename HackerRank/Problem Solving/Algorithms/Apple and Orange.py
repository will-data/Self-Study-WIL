#!/bin/python3

import os
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    return([sum(s <= a+x <= t for x in apples),
            sum(s <= b+y <= t for y in oranges)])

if __name__ == '__main__':
    s, t = map(int,input().split())
    a, b = map(int,input().split())
    m, n = map(int,input().split())
    apples = list(map(int,input().split()))
    oranges = list(map(int,input().split()))

    result = countApplesAndOranges(s, t, a, b, apples, oranges)
    print(result[0])
    print(result[1])
