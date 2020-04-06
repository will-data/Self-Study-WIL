#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    hourglasses = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    hourglasses = []

    for i in range(len(arr)-2):
        for j in range(len(arr[i])-2):
            hourglass = sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3])
            hourglasses.append(hourglass)
    print(max(hourglasses))
