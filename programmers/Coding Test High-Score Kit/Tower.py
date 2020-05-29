def solution(heights):
    answer = [0]
    for i, height in enumerate(heights[1:]):
        i += 1;
        found = False
        for j in range(1, i + 1):
            if heights[i - j] > height:
                answer.append(i - j + 1);
                found = True
                break
        if not found:
            answer.append(0)

    return answer