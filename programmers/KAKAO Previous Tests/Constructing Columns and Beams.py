from operator import itemgetter


def solution(n, buildFrames):
    struc = set()

    def check(struc):
        for x, y, a in struc:
            if a == 0:
                if not (y == 0 or not {(x, y - 1, 0), (x, y, 1), (x - 1, y, 1)}.isdisjoint(struc)):
                    return False
            else:
                if not (not {(x, y - 1, 0), (x + 1, y - 1, 0)}.isdisjoint(struc) or {(x - 1, y, 1),
                                                                                     (x + 1, y, 1)}.issubset(struc)):
                    return False
        return True

    for x, y, a, b in buildFrames:
        if b == 1:
            # Constructing column
            if a == 0:
                if (y == 0 or not {(x, y - 1, 0), (x, y, 1), (x - 1, y, 1)}.isdisjoint(struc)):
                    struc.add((x, y, 0))
            # Constructing beam
            else:
                if (not {(x, y - 1, 0), (x + 1, y - 1, 0)}.isdisjoint(struc) or {(x - 1, y, 1), (x + 1, y, 1)}.issubset(
                        struc)):
                    struc.add((x, y, 1))
        elif b == 0:
            struc.discard((x, y, a))
            if not check(struc):
                struc.add((x, y, a))

    return sorted(list(map(list, struc)), key=itemgetter(0, 1, 2))