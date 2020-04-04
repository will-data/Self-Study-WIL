numerator, denominator = map(int, input().split())
p = numerator / denominator
n = int(input())

geom = lambda p, n: (1-p)**(n-1)*p
print(round(geom(p,n),3))