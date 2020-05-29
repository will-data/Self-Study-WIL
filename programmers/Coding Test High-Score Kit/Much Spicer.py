import heapq
def solution(scoville, K):
    mixCnt = 0; heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) >=2:
            mixCnt += 1
            mix1 = heapq.heappop(scoville); mix2 = heapq.heappop(scoville)
            heapq.heappush(scoville, mix1+mix2*2)
        else:
            return -1

    return mixCnt