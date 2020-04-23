import time
from math import floor

# Algorithm with O(n) time complexity
def checkPrimeAll(n):
    if n ==1: return('Not prime')
    for i in range(2,n):
        if n%i ==0:
            return('Not prime')
    return('Prime')

# Algorithm with O(sqrt(n)) time complexity
def checkPrimeSqrt(n):
    if n ==1: return('Not prime')
    for i in range(2,floor(n**(1/2))+1):
        if n%i ==0:
            return('Not prime')
    return('Prime')

T = int(input())
# Check time by using checkPrimeAll
# It took 5.0067901611328125e-05 seconds for Sample Test case 0
# It took 4.482269287109375e-05 seconds for Sample Test case 1
# For case checking big 5 numbers including one prime number(115249, 62015456165, 1945165169, 842615186651, 151655188498157), it took 0.010605335235595703 seconds.
start_time = time.time()

# for i in range(T):
#     n = int(input())
#     print(checkPrimeAll(n))
# print('{} seconds'.format(time.time()-start_time))

# Check time by using checkPrimeSqrt
# It took 7.367134094238281e-05 seconds for Sample Test case 0
# It took 5.698204040527344e-05 seconds for Sample Test case 1
# For case checking big 5 numbers including one prime number(115249, 62015456165, 1945165169, 842615186651, 151655188498157), it took 0.00014400482177734375 seconds, which is much faster than O(n) algorithm
for i in range(T):
    n = int(input())
    print(checkPrimeSqrt(n))
#print('{} seconds'.format(time.time()-start_time))