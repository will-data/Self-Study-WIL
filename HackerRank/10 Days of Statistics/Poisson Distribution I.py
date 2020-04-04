import math

p = float(input())
n = int(input())

factorial = lambda n: 1 if n==1 else n*factorial(n-1)

poisson = lambda p, n: p**n*math.exp(-p)/factorial(n)
print(poisson(p,n))