#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    cost_dict = {}
    for num, cost in enumerate(cost):
# Since there can be dupliate of price but only has a unique solution, I can make it faster through line below
        if cost in cost_dict:
            if cost*2 == money:
                print(str(cost_dict[cost]+1),str(num+1))
            else:
                pass
        elif money-cost in cost_dict:
            print(str(cost_dict[money-cost]+1),str(num+1))
        else:
            cost_dict[cost] = num

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
