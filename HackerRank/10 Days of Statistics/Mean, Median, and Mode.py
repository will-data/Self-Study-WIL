# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
X = list(map(int, input().split()))
X.sort()

# Solution without import Package
## mean
X_mean = round(sum(X)/N,1)
## median
if N%2 != 0:
    X_median = X[int(N/2-0.5)]
else:
    X_median = round((X[int(N/2-1)]+X[int(N/2)])/2, 1)
## mode
X_dict = dict((x, X.count(x)) for x in X)
X_mode = max(X_dict, key=X_dict.get)

# Solution with importing package
import numpy as np
from scipy import stats

X_mean = np.mean(X)
X_median = np.median(X)
X_mode = stats.mode(X)[0][0]

print(X_mean)
print(X_median)
print(X_mode)
#print(X_dict)