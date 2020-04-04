import math

p_1, p_2 = map(float, input().split())

factorial = lambda n: 1 if n==1 else n*factorial(n-1)
# Use same fucntion of prior probelm, Poisson Distribution I
## Actually, this functions is not needed in the solution.
poisson = lambda p, n: p**n*math.exp(-p)/factorial(n)

print(160+40*(p_1+p_1**2))
print(128+40*(p_2+p_2**2))
