def searching(s):
    # [] {} () 의미
    arr = [0, 0, 0]

    for i in range(len(s)):
        if s[i] == ')' and arr[2] != 1:
            arr[2] = -1
            break
        elif s[i] == '}' and arr[1] != 1:
            arr[1] = -1
            break
        elif s[i] == ']' and arr[0] != 1:
            arr[0] = -1
            break

        for j in range(i + 1, len(s)):
            if s[i] == '(' and s[j] == ')':
                arr[2] = 1
                break
            elif s[i] == '{' and s[j] == '}':
                arr[1] = 1
                break
            elif s[i] == '[' and s[j] == ']':
                arr[0] = 1
                break
        
    if -1 in arr:
        return 0
    else:
        return 1
        
        
def solution(s):
    l = len(s)

    stack = []
    for i in s:
        stack.append(i)
    
    result = 0
    for i in range(l):
        # 괄호 검사
        result += searching(stack)

        # 문자열 회전 구현
        # 맨 앞의 요소 제거하고 스택에 추가
        element = stack[0]
        stack.remove(element)
        stack.append(element)
        # print(stack)
        
    return result

print(solution('}]()[{'))