n = int(input())
a = list(map(int, input().split()))

numSwaps = 0;
for i in range(n):
    # Setting range to n-i-1 works because at ith scanning, the ith samller number goes to a[n-i].
    for j in range(n - i - 1):
        if (a[j] > a[j + 1]):
            numSwaps += 1
            a[j], a[j + 1] = a[j + 1], a[j]

firstElement = a[0];
lastElement = a[-1]

print("Array is sorted in {} swaps.".format(numSwaps))
print("First Element: {}".format(firstElement))
print("Last Element: {}".format(lastElement))
