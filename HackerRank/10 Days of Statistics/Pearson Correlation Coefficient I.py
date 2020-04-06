n = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))

# Define function to calculate mean and std by myself.
mean = lambda X: sum(X)/len(X)
std = lambda X: (sum([(x-mean(X))**2 for x in X])/len(X))**(1/2)

numerator = 0
for i in range(n):
    numerator += (X[i]-mean(X))*(Y[i]-mean(Y))
print(round(numerator/(n*std(X)*std(Y)),3))