def sepBalanced(q):
    sepN = 1 if q[0] == '(' else -1;
    i = 0
    while sepN != 0 and i < len(q):
        i += 1
        sepN = sepN + 1 if q[i] == '(' else sepN - 1
    return q[:(i + 1)], q[(i + 1):]


def checkCorrect(q):
    checkStack = 0
    for s in q:
        if s == '(':
            checkStack += 1
        else:
            checkStack -= 1
        if checkStack < 0:
            return False
    return True


def solution(p):
    if not p:
        return p
    if checkCorrect(p):
        return p

    u, v = sepBalanced(p)
    if checkCorrect(u):
        return u + solution(v)
    else:
        return '(' + solution(v) + ')' + "".join([')' if i == '(' else '(' for i in u[1:-1]])

