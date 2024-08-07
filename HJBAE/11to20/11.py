def solution(s):
    stack = []
    
    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    
    if stack:
        return 0
    else:
        return 1
    
print(solution("baabaa"))
print(solution("cdcd"))
# 1 0 
# 2024 08 05 AM 03:02
# I'm dog 취한 상태 

