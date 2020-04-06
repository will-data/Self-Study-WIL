import math
import os
import random
import re
import sys

# Define function to convert base-10 integer to base-2 string, wihtout importing any package
def intToBinary(n):
    if n <=1:
        return(str(n))
    else:
        binary = ''
        while n != 1:
            binary = str(n%2) + binary
            n = n//2
        return('1'+binary)

# Can convert base-10 integer to base-2 string using python's base function, bin().
# str(bin(n)[2:])

# My orginial solution to count Max Consecutvie 1s, using two inner loops.
# def countMaxConsecutive(binary):
#    counts = []
#    for i in range(len(binary)):
#        count = 1; j = i+1
#        if binary[i] =='1':
#            while j < (len(binary)):
#                if binary[j] =='1':
#                    j+=1; count +=1
#                else:
#                    break
#            counts.append(count)
#        else:
#            counts.append(count)
#            pass
#  return max(counts)

# Eaiser solution got from discussions. just divide string with '0', and count the length of consecutive '1's subgroup
# max[len(num) for num in binary.split('0')]
# max([len(num) for num in binary])

if __name__ == '__main__':
    n = int(input())
#    print(countMaxConsecutive(intToBinary(n)))
    binary = str(bin(n)[2:]).split('0')
    print(max([len(num) for num in binary]))
