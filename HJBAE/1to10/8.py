def solution(gwalho):
    stack =[]
    for char in gwalho:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return not stack

print(solution("()"))
print(solution("(())(())()"))
print(solution("())"))