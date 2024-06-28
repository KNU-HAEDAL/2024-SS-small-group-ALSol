def is_valid(s):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in bracket_map.values():  
            stack.append(char)
        elif char in bracket_map.keys():  
            if stack == [] or bracket_map[char] != stack.pop():  
                return False
    return stack == [] 

def solution(s):
    answer = 0
    for i in range(len(s)):
        if is_valid(s[i:] + s[:i]):  
            answer += 1
    return answer

print(solution("[](){}"))  # 3
