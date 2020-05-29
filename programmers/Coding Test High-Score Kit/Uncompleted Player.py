from collections import Counter
def solution(participant, completion):
    uncompCount = Counter(participant)- Counter(completion)
    return list(uncompCount.keys())[0]