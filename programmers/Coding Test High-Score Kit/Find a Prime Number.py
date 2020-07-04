import itertools
import math


def checkPrime(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    else:
        for i in range(2, (math.floor(number ** (1 / 2) + 1))):
            if number % i == 0:
                return False
        return True


def solution(numbers):
    answer = 0
    perNs = set(map(int, [number for number in numbers]))
    perNmax = set(map(int, (map(''.join, itertools.permutations([i for i in numbers])))))
    for perN in perNmax:
        for i in range(2, len(numbers)):
            perNs.add(int(str(perN)[:i]))
    perNs.update(perNmax)

    for perN in perNs:
        if checkPrime(perN):
            answer += 1

    return answer