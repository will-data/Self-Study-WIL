
def fibonacci(n):
# Solution below is recursive, but it takes too much time when n is large
#    if n in [0,1]:
#        return n
#    else:
#        return fibonacci(n-1)+fibonacci(n-2)
# Therefore, using memories to shorten time
    fibo_memory = {0:0, 1:1}
    if n<=2:
        return fibo_memory[n]
    else:
        for i in range(2, n):
            fibo_memory[i] = fibo_memory[i-1]+fibo_memory[i-2]
        return fibo_memory[n-1] + fibo_memory[n-2]

n = int(input())
print(fibonacci(n))