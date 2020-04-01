# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
X = list(map(int, input().split()))
X.sort()


def median(X):
    n=len(X)
    if n%2 ==0:
        return((X[n//2-1]+X[n//2])/2)
    else:
        return(X[n//2])

print(int(median(X[:n//2])))
print(int(median(X)))
print(int(median(X[(n+1)//2:])))