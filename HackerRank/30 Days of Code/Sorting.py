#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

allNumSwaps = 0
for i in range(n):
    numSwaps = 0
    for j in range(n-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            numSwaps += 1
    if numSwaps ==0: break
    allNumSwaps += numSwaps


print('Array is sorted in {} swaps.'.format(allNumSwaps))
print('First Element:', a[0])
print('Last Element:', a[-1])