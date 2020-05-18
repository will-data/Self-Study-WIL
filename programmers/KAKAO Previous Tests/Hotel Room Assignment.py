def solution(k, room_number):
    roomDict = {};
    answer = []
    for roomNum in room_number:
        if roomNum not in roomDict:
            answer.append(roomNum)
            roomDict[roomNum] = roomNum + 1
        else:
            updateNums = [roomNum]
            roomNum = roomDict[roomNum]
            while roomNum in roomDict:
                updateNums.append(roomNum)
                roomNum = roomDict[roomNum]
            answer.append(roomNum)
            roomDict[roomNum] = roomNum + 1
            for updateNum in updateNums:
                roomDict[updateNum] = roomNum + 1

    return answer