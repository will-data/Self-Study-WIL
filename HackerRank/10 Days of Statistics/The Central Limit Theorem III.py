import math

n = int(input())
mu = float(input())
sigma = float(input())
confidence_level = float(input())
z = float(input())

# Since I can't import scipy and statistics package here, I'll use math package's erf instead.
## I don't need this function for this problem.
cdf = lambda x, mu, sigma: 0.5 * (1 + math.erf((x - mu) / (sigma * (2 ** 0.5))))

print(mu-z*sigma/n**(1/2))
print(mu+z*sigma/n**(1/2))