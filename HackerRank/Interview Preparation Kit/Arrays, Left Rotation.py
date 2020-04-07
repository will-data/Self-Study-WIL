n, d = map(int, input().split())
a = list(map(int, input().split()))

def array_left_rotation(a, n, d):
    return([a[(i+d)%n] for i in range(n)])

answer = array_left_rotation(a, n, d);
print(*answer, sep=' ')