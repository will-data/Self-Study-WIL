from collections import defaultdict
def solution(tickets):
    ticketDict = defaultdict(list);
    for start, end in tickets:
        ticketDict[start].append(end)
    for start in ticketDict:
        ticketDict[start].sort(reverse=True)

    current = 'ICN';
    ticketCnt = len(tickets);
    journey = ['ICN']

    def backJourney(ticketDict, current, journey, ticketCnt):
        ticketCnt += 1
        ticketDict[journey[-2]].insert(0, current)
        journey.pop()
        current = journey[-1]
        if ticketDict[current] == sorted(ticketDict[current], reverse=True):
            # print("ahh")
            return backJourney(ticketDict, current, journey, ticketCnt)
        else:
            return [ticketDict, current, journey, ticketCnt]

    def journeyTry(ticketDict, current, journey, ticketCnt):
        while ticketDict[current] != []:
            current = ticketDict[current].pop()
            journey = journey + [current]
            ticketCnt -= 1
            # print(ticketDict, current, journey, ticketCnt)
        if ticketCnt == 0:
            return journey
        else:
            backT = backJourney(ticketDict, current, journey, ticketCnt)
            # print(backT)
            return journeyTry(backT[0], backT[1], backT[2], backT[3])

    answer = journeyTry(ticketDict, current, journey, ticketCnt)
    return answer