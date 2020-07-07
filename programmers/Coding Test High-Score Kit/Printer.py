def solution(priorities, location):
    # Make stack by reversing prioirites and save initial index
    printStack = [(i,p) for i,p in enumerate(priorities[::-1])]
    cnt = 0; location = len(priorities) -location - 1
    while True:
        current = printStack.pop()
        if any(other[1] > current[1] for other in printStack):
            printStack.insert(0,current)
        else:
            cnt += 1
            if current[0] == location:
                return cnt