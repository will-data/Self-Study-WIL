import math

# My First Solution
def solution(progresses, speeds):
    completes = []
    for progress, speed in zip(progresses, speeds):
        completes.append(math.ceil((100 - progress) / speed))

    answer = [];
    completes = completes[::-1]
    while completes:
        done = 1;
        current = completes.pop();
        check = True
        while check and completes:
            next = completes.pop();
            if next <= current:
                done += 1
            else:
                check = False;
                completes.append(next)
        answer.append(done)

    return answer


# Better solution
import math

def solution(progresses, speeds):
    answer = []
    for progress, speed in zip(progresses, speeds):
        if not answer or answer[-1][0] < math.ceil(math.ceil((100-progress)/speed)):
            answer.append([math.ceil(math.ceil((100-progress)/speed)),1])
        else:
            answer[-1][1] +=1

    return [i[1] for i in answer]