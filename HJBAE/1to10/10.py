def solution(demical):
    stack = []
    
    if demical == 0:
        return "0"
    
    while demical > 0:
        remainder = demical % 2   #나머지
        stack.append(str(remainder))
        demical = demical // 2

    binary = ""
    while stack:    #스택이 빈 상태 아닐 때까지 반복하는 루프
        binary += stack.pop()

    return binary
    
print(solution(20))
print(solution(32))

"""파이썬에서는 빈 리스트는 False로 평가
요소가 있는 리스트는 True로 평가
while stack:은 스택에 요소가 있는 동안 루프를 실행"""