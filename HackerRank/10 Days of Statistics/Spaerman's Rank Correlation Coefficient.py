n = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))

mean = lambda X: sum(X)/len(X)
std = lambda X: (sum([(x-mean(X))**2 for x in X])/len(X))**(1/2)
# Define function to caluculate rank of elemts in the list with sort() funtion.
def rank_list(X):
    X_rank = [0] * len(X)
    for i, x in enumerate(sorted(list(range(len(X))), key = lambda y: X[y])):
        X_rank[x] = i
    return(X_rank)

# Use same code with prblem 'Pearson Correlation Coefficient I'
X_rank = rank_list(X); Y_rank = rank_list(Y)
numerator = 0

for i in range(n):
    numerator += (X_rank[i]-mean(X_rank))*(Y_rank[i]-mean(Y_rank))
print(round(numerator/(n*std(X_rank)*std(Y_rank)),3))