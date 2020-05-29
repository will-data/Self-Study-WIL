def solution(bridge_length, weightLim, truck_weights):
    time = 0;
    truck_weights = truck_weights[::-1]
    currents = [truck_weights.pop()];
    times = [1]
    while truck_weights:
        time += 1
        if times[-1] + bridge_length <= time:
            currents.pop();
            times.pop()
        if truck_weights[-1] + sum(currents) <= weightLim:
            currents.insert(0, truck_weights.pop())
            times.insert(0, time)
    while currents:
        time += 1
        if times[-1] + bridge_length <= time:
            currents.pop();
            times.pop()
    return time
