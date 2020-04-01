import math
p, q = map(float, input().split())
p_scaled = p/(p+q); q_scaled = q/(p+q)

# Interesting code to execute factorial
## def fact(n):
##     return 1 if n ==0 else n*fact(n-1)

def comb(n,m):
    return(math.factorial(n)/(math.factorial(m)*math.factorial(n-m)))

def binom(p,n_p,n=6):
    return float(comb(n,n_p)* p**n_p * (1-p)**(n-n_p))

# Sum by using 'for'
#answer = 0
#for n_p in range(3,7):
#    answer += binom(p_scaled,n_p)

# Another summing solution
answer = sum(binom(p_scaled,n_p) for n_p in range(3,7))

print(round(answer,3))