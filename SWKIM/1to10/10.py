def solution(s):
    answer = 0
    check = ['(', '{', '[']
    size = len(s)

    for i in range(size):
        cnt = 0
        stack = []
        for j in range(size):
            if s[(i+j)%size] in check:
                stack.append(s[(i+j)%size])
            elif s[(i+j)%size] == ')':
                if len(stack)!=0 and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(s[(i+j)%size])
            elif s[(i+j)%size] == '}':
                if len(stack)!=0 and stack[-1] == '{':
                    stack.pop()
                else:
                    stack.append(s[(i+j)%size])
            elif s[(i+j)%size] == ']':
                if len(stack)!=0 and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(s[(i+j)%size])
        
        if len(stack) == 0:
            answer += 1
    
    return answer

