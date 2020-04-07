import math
import os
import random
import re
import sys
from collections import Counter

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    count_diff = Counter(a)
# There is a difference between subtract and '-'. The latter only returns keys with 0+ vlaues.
    count_diff.subtract(Counter(b))
    return sum([abs(count_diff[i]) for i in count_diff])

if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()
    b = input()

    res = makeAnagram(a, b)
    print(res)
#    fptr.write(str(res) + '\n')
#    fptr.close()
