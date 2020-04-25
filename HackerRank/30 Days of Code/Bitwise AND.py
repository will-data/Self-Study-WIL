#!/bin/python3

import math
import os
import random
import re
import sys


# Solution below was my first code, but it is not fast enough to pass all the test cases.
#if __name__ == '__main__':
#    t = int(input())
#    for t_itr in range(t):
#        maxPossible = 0
#        nk = input().split()
#        n = int(nk[0]); k = int(nk[1])
#        for i in range(1,n):
#            for j in range(i+1,n+1):
#                bitAND = i & j
#                if bitAND == k-1:
#                    maxPossible = k-1; break
#                elif bitAND > maxPossible and bitAND < k:
#                    maxPossible = bitAND
#        print(maxPossible)


# Therefore, I read discussions on HackerRank, and found a elegmnt answer. Detailed instruction is written by 'gvandam', in the thread.
if __name__ == '__main__':
    t= int(input())
    for t_itr in range(t):
        n, k = map(int, input().split())
        print(k-1 if ((k-1) | k) <= n else k-2)
