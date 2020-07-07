def solution(budgets, M):
    left_lim = 0;
    right_lim = max(budgets)
    while left_lim <= right_lim:
        #        print(left_lim, right_lim)
        lim = (left_lim + right_lim) // 2
        if sum([i if i <= lim else lim for i in budgets]) > M:
            right_lim = lim - 1
        else:
            left_lim = lim + 1

    return right_lim