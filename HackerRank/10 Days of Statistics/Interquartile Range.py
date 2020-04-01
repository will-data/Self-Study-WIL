import itertools

N = int(input())
X = list(map(int,input().split()))
F = list(map(int, input().split()))
X_full = []
# for i in range(N):
#     X_full += itertools.repeat(X[i],F[i])
# You can do repetation without using itertools package, just like below
for i in range(N):
    X_full += [X[i]] * F[i]
X_full.sort()
n_full = len(X_full)

# used my codes from prior problem, quantiles
## Made mistake once in here, didn't return the float value. if you return the value without converting it to flaot, you'll fail.
def median_my(X):
    n=len(X)
    if n%2 ==0:
        return(float((X[n//2-1]+X[n//2])/2))
    else:
        return(float(X[n//2]))

IQR = median_my(X_full[(n_full+1)//2:])-median_my(X_full[:n_full//2])
print(round(IQR,1))

