def solution(s):
    stack = []
    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)

    if len(stack) == 0:
        return 1
    else:
        return 0


# print(solution('baabaa'))
# print(solution('cdcd'))