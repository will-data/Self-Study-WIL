def solution(n, losts, reserves):
    answer = n - len(losts)
    losts = set(losts);
    reserves = set(reserves)
    for lost in losts.copy():
        if lost in reserves.copy():
            reserves.remove(lost);
            losts.remove(lost)
            answer += 1

    losts = list(losts);
    check = 0
    while losts and check < 100:
        if not reserves:
            return answer
        else:
            lost = losts.pop();
            check += 1
            if (lost - 1) in reserves and (lost + 1) not in reserves:
                reserves.discard(lost - 1);
                answer += 1
            elif (lost - 1) not in reserves and (lost + 1) in reserves:
                reserves.discard(lost + 1);
                answer += 1
            elif (lost - 1) in reserves and (lost + 1) in reserves:
                losts.insert(0, lost)
            else:
                pass

    return (answer + len(losts))