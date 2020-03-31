import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    for i in range(10):
        i +=1
#       print(str(n) + ' x ' + str(i)  + ' = ' + str(n*(i)))
        # Other Solution using .format
        print("{} x {} = {}".format(n, i, (n*i)))
        # Another Solution using just print
        #print(n,'x',i,'=',n*i)