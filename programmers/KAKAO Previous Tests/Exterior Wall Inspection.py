import itertools


def solution(n, weak, dist):
    if len(weak) == 1:
        return 1

    dist.sort(reverse=True)

    friendsCnt = 0
    while friendsCnt < len(dist):
        friendsCnt += 1
        friendPers = []
        for i in itertools.permutations(dist, friendsCnt):
            friendPers.append(list(i))
        for friendPer in friendPers:
            j = 0
            while j < len(weak):
                checkWeak = weak[j:] + [w + n for w in weak[:j]]

                start = checkWeak[0];
                friendIndex = 0
                for check in checkWeak[1:]:
                    if friendIndex < friendsCnt:
                        if start + friendPer[friendIndex] < check:
                            start = check;
                            friendIndex += 1
                if friendIndex < friendsCnt:
                    return friendsCnt

                j += 1

    return -1