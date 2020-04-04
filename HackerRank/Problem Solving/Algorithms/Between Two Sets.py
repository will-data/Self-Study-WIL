#!/bin/python3

import os
import sys
import math

# At first, define function to calculate LCM(Least Common Multiple) and GCD(Greatest Common Divider)
## Be careful of the case when lenth of input a,b is 1.... ToT
def gcd(X):
    if len(X) > 2:
        return(gcd([gcd(X[1:]),X[0]]))
    elif len(X) ==1:
        return(X[0])
    else:
        while X[1] > 0:
            X = [X[1],X[0]%X[1]]
        return X[0]

def lcm(X):
    if len(X) > 2:
        return(lcm([lcm(X[1:]),X[0]]))
    elif len(X) ==1:
        return(X[0])
    else:
        return(int(X[0]*X[1]/gcd(X)))

# Complete the getTotalX function below.
def getTotalX(a, b):
    gcd_b = gcd(b)
    lcm_a = lcm(a)
    if gcd_b % lcm_a ==0:
        temp = gcd_b//lcm_a
        return sum( temp % (i+1) == 0 for i in range(temp))

#최대공약수가 0이거나, 최소공배수가 100보다 크거나

    else:
        return 0

if __name__ == '__main__':
    n,  m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    print( getTotalX(a,b) )
