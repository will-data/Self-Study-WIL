def solution(citations):
    citations.sort(reverse= True)
    answer = len(citations)
    while True:
        if citations[answer-1] >= answer:
            return answer
        else:
            answer -= 1
            if answer < 0:
                break
    return 0