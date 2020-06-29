def solution(answers):
    score = [0,0,0];
    answer1 = [1,2,3,4,5]
    answer2 = [2,1,2,3,2,4,2,5]
    answer3 = [3,3,1,1,2,2,4,4,5,5]
    for i, answer in enumerate(answers):
        if answer == answer1[i%5]:
            score[0] += 1
        if answer == answer2[i%8]:
            score[1] += 1
        if answer == answer3[i%10]:
            score[2] += 1
    mScore = max(score)
    return [(i+1) for i, j in enumerate(score) if j == mScore]


