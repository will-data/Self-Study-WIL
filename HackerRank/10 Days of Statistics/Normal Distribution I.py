import math

mean, std = map(float, input().split())
a = float(input())
b, c = map(float, input().split())
standard = lambda x: (x-mu)/sigma

# Since I can't import scipy and statistics package here, I'll use math package's erf instead.
cdf = lambda x: 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))

print(round(cdf(a), 3))
print(round(cdf(c)-cdf(b),3))


