def solution(s):
    stack = [ ]

    for i in s:
        if i == ')':
            if len(stack) != 0:
                stack.pop()
            else:
                return False
        elif i == '(':
            stack.append(i)

    if len(stack) == 0:
        return True
    else:
        return False

print(solution('(())()')) # 반환값 : True
print(solution('((())()')) # 반환값 : False