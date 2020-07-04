import itertools
def solution(checks):
    answers = set()
    for x in list(itertools.permutations(range(1, 10), 3)):
        answers.add(int(''.join(str(e) for e in x)))

    for check, s, b in checks:
        newAnswers = set()
        for answer in answers:
            sCheck = (str(check)[0] == str(answer)[0]) + (str(check)[1] == str(answer)[1]) + (
                        str(check)[2] == str(answer)[2])
            bCheck = 6 - len(set([i for i in str(check) + str(answer)])) - sCheck
            if s == sCheck and b == bCheck:
                newAnswers.add(answer)
        answers = newAnswers

    return len(answers)