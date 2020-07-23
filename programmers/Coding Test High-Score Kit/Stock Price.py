def solution(prices):
    answers = []
    for i, price in enumerate(prices):
        j = 1; find = False
        while i+j < len(prices):
            if prices[i+j] < price:
                find = True; break
            j += 1
        if find:
            answers.append(j)
        else:
            answers.append(j-1)

    return answers