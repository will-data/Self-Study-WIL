import math
import os
import random
import re
import sys


if __name__ == '__main__':
    N = int(input())
    nameList = []
    for N_itr in range(N):
        firstNameEmailID = input().split()
        firstName = firstNameEmailID[0]
        emailID = firstNameEmailID[1]
        if '@gmail.com' in emailID:
            nameList.append(firstName)
    print (*sorted(nameList), sep='\n')