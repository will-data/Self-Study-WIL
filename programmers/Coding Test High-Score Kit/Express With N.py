def solution(N, number):
    if N == number: return 1
    setList = [set()]
    setList.append(set([N])); i=2
    while i<9:
        setTemp = [N*int("1"*i)]
        j = 1
        while j < i:
            for a in setList[j]:
                for b in setList[i-j]:
                    setTemp += [a*b,a-b,a+b,a//b]
            j += 1
        setTemp = set(setTemp); setTemp.discard(0)
        if number in setTemp: return i
        setList.append(setTemp); i += 1
    return -1