from collections import deque

def solution(A, B):
    answer = 0
    A.sort(reverse = True)
    B.sort(reverse = True)
    A = deque(A)
    B = deque(B)
    
    # B의 숫자가 A보다 크면 +1과 해당 수 삭제, 아니면 가장 작은 수 삭제
    while B:
        num = A.popleft()

        if B[0] > num:
            B.popleft()
            answer += 1
        else:
            B.pop()
        
    return answer
