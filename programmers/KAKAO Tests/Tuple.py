def solution(st):
    outSets = []
    for s in st[2:-2].split('},{'):
        outSets.append(set(map(int,s.split(','))))
    outSets.sort(key=len)
    if len(outSets) == 1:
        return [list(outSets[0])[0]]
    else:
        answer = [list(outSets[0])[0]];
        before = outSets[0]; current = outSets[1]; i = 1;
        while i < len(outSets)-1:
            answer.append(list(current.difference(before))[0])
            before, current = current, outSets[i+1]
            i += 1
        answer.append(list(current.difference(before))[0])

        return answer