import math

mean, std = map(float, input().split())
a = float(input())
b = float(input())

# Since I can't import scipy and statistics package here, I'll use math package's erf instead.
cdf = lambda x: 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))

# Be careful for the output shape. You sould *100 to your probability since the answer is needed to be transformed in %.
print(round((1-cdf(a))*100, 2))
print(round((1-cdf(b))*100, 2))
print(round(cdf(b)*100, 2))