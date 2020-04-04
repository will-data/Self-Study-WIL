#!/bin/python3
import os
import sys

#
# Complete the simpleArraySum function below.
# Classic soluntion with defining funciton
#def simpleArraySum(ar):
#    ar_sum = 0
#    for i in ar:
#        ar_sum += i
#    return ar_sum
# Easier solution

simpleArraySum = lambda X: sum(X)

if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = simpleArraySum(ar)
    print(result)
#    fptr.write(str(result) + '\n')

#    fptr.close()