numerator, denominator = map(int, input().split())
p = numerator / denominator
n = int(input())

geom = lambda p, n: (1-p)**(n-1)*p
# Only below part changed from Geometric Distribution I's solution.
# I summed up all probability for int i, where i<=n.
print(round(sum(geom(p,i+1) for i in range(n)),3))