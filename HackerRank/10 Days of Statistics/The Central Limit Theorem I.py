import math

maximum_weight = float(input())
n = int(input())
mu = float(input())
sigma = float(input())

# Since I can't import scipy and statistics package here, I'll use math package's erf instead.
cdf = lambda x, mu, sigma: 0.5 * (1 + math.erf((x - mu) / (sigma * (2 ** 0.5))))

print(round(cdf(maximum_weight, mu*n, sigma*n**(1/2)),4))