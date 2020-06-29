def solution(numbers, target):
    answerSet = [numbers[0],-numbers[0]]
    for number in numbers[1:]:
        answerSet = [number + i for i in answerSet] + [-number + i for i in answerSet]
    return sum([target == i for i in answerSet])