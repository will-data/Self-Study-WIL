# My original solution
def solution(phone_book):
    answer = True
    for phone in phone_book:
        for otherPhone in phone_book:
            if len(otherPhone) > len(phone):
                if otherPhone[:len(phone)] == phone:
                    answer = False
                    return answer
    return answer

# Interesting approach found in other's solutions
from itertools import combinations as c
def solution(phoneBook):
    answer = True
    sortedPB = sorted(phoneBook, key= len)
# This method, itertools.combinations seems very useful
    for (a,b) in c( sortedPB,2):
        if a == b[:len(a)]:
            answer = False
    return answer