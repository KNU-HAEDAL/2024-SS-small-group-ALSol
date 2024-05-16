# def solution(decimal):
#     return format(decimal, 'b')

def solution(deciaml):
    num = deciaml
    stack = []
    while(num != 1):
        stack.append(num%2)
        num = num // 2
    stack.append(num)
    
    answer = ''
    while(stack):
        answer += str(stack.pop())
    
    return answer



