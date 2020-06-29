def solution(numbers):
    numSort = []
    for number in numbers:
        temp = list(str(number))
        temp = ([len(temp)] + list(str(number))*5)[:6]
        numSort.append(temp)
    numSorted = sorted(numSort, key=lambda k: (int(k[1]),int(k[2]),int(k[3]),int(k[4])), reverse=True)
    answer = ''
    for num in numSorted:
        answer += ''.join(num[1:(num[0]+1)])
    return(str(int(answer)))