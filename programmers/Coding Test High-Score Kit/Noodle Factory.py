import heapq


def solution(stock, dates, supplies, k):
    supplyCnt = 0;
    available = [];
    dates = dates[::-1];
    date = 0;
    nextd = 0
    supplies = supplies[::-1]

    while date < k and dates:
        date, nextd = nextd, dates.pop()
        stock -= nextd - date
        while stock < 0:
            stock -= heapq.heappop(available)
            supplyCnt += 1
        heapq.heappush(available, -supplies.pop())

    stock -= k - nextd
    while stock < 0:
        stock -= heapq.heappop(available)
        supplyCnt += 1

    return supplyCnt