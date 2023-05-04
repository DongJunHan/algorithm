def solution(s):
    answer = -1
    stack = []
    l = 0
    for i in range(len(s)):
        if len(stack) > 0 and  s[i] == stack[len(stack)-1]:
            stack.pop()
        else:
            stack.append(s[i])

    if len(stack) == 0:
        return 1
    else:
        return 0