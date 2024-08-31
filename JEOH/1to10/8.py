def solution(a):
    stack=[]
    for i in a:
        if i=="(":
            stack.append(i)
        elif i==")":
            if not stack:
                return False
            else:
                stack.pop()
    if stack:
        return False
    else:
        return True
