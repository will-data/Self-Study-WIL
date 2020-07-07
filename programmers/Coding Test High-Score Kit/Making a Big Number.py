
# My own solution hat doesn't use stack but index
def solution(number, k):
    i = 0; forward = True
    while k > 0:
        if i < 0 or number[i] == "9":
            forward = True
        elif i >= len(number) -1:
            return number[:-k]
        else:
            if number[i] < number[i+1]:
                number = number[:i] + number[(i+1):]
                k -= 1; forward = False
        i = i+1 if forward else i-1
    return number

# Another solution using stack. This is much faster because it doesn't need to check end of the prior number.
def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)