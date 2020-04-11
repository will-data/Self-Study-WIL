#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    hh = int(s[:-2].split(':')[0])
    hh = str(hh % 12 + (s[-2:] == 'PM') * 12)
    if len(hh) == 1:
        hh = '0' + hh
    return(str(hh)+s[2:-2])

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()