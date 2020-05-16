import itertools


def solution(user_ids, banned_ids):
    def checkSin(user_id, banned_id):
        if len(user_id) != len(banned_id):
            return False
        for s in range(len(banned_id)):
            if banned_id[s] == '*' or user_id[s] == banned_id[s]:
                pass
            else:
                return False
        return True

    userPers = itertools.permutations(user_ids, len(banned_ids))
    checkList = []

    for userPer in userPers:
        check = True
        for i, user in enumerate(userPer):
            if not checkSin(user, banned_ids[i]):
                check = False;
                break
        if check and sorted(list(userPer)) not in checkList:
            checkList.append(sorted(list(userPer)))

    return len(checkList)