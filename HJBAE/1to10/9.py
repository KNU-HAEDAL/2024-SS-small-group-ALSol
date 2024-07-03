def gwalho_pair(s):
    stack = []
    match_pair = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack[-1] != match_pair[char]:
                return False
            stack.pop()
    
    return not stack

def rotate_gwalho(s):
    return s[1:] + s[0]

def solution(s):
    count = 0
    n = len(s)
    
    for i in range(n):
        if gwalho_pair(s):
            count += 1
        s = rotate_gwalho(s)
    
    return count

# 테스트 예시
print(solution("[](){}"))  # 3
print(solution("}]()[{"))  # 2
print(solution("[)(]"))    # 0
print(solution("}}}"))     # 0
print(solution(rotate_gwalho("]()[")))    #2