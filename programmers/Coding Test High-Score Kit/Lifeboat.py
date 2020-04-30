def solution(people, limit):
    boatCount = 0
    people.sort()
    i = 0; j = len(people)-1
    while i < j:
        if people[i] + people[j] > limit:
            j -=1; boatCount +=1
        else:
            i +=1; j -=1; boatCount +=1
    if i == j: boatCount += 1
    return(boatCount)
