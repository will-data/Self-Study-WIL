import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())
# My Original code
    # if N%2==1:
    #     print('Weird')
    # elif N>=6 and N<=20:
    #     print('Weird')
    # else:
    #     print('Not Weird')
# More creative code from discussions
    out = "Weird"
    if N%2==0 and (N<6 or N>20): out = "Not " + out
    print(out)