N = int(input())
X = list(map(int, input().split()))
W = list(map(int, input().split()))

weighted_sum = 0
# sum without zip
for n in range(N):
    weighted_sum += X[n] * W[n]

# sum with using zip, this is much more easy
weighted_sum = sum([x * w for x, w in zip(X, W)])

print(round(weighted_sum / sum(W), 1))
