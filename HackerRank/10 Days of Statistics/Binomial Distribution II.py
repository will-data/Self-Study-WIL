import math
p, n = map(int, input().split())
p_scaled = float(p/100)

# Interesting code to execute factorial
## def fact(n):
##     return 1 if n ==0 else n*fact(n-1)

def comb(n,m):
    return(math.factorial(n)/(math.factorial(m)*math.factorial(n-m)))

def binom(p,n_p,n):
    return float(comb(n,n_p)* p**n_p * (1-p)**(n-n_p))

answer_1 = sum(binom(p_scaled,n_p,n) for n_p in range(3))
answer_2 = sum(binom(p_scaled,n_p,n) for n_p in range(2,n+1))


print(round(answer_1,3))
print(round(answer_2,3))