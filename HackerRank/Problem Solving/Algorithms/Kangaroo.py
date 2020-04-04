
def kangaroo(x1, v1, x2, v2):
    if v1 > v2 and (x2-x1) % (v1-v2) == 0:
        return 'YES'
    else:
        return 'NO'
x1, v1, x2, v2 = map(int,input().split())
print( kangaroo(x1, v1, x2, v2))
