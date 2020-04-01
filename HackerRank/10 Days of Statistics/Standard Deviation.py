import math

N = int(input())
X = list(map(float, input().split()))

mean = sum(X)/N
sd = sum(pow(x-mean,2) for x in X)/float(N)
#print(round(math.sqrt(sd),1))

#Also can make this in one-line without using package
print(round((sum((x-sum(X)/N)**2 for x in X)/N)**0.5,1))

