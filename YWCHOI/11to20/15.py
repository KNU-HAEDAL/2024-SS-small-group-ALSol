from collections import deque

def solution(N, K):
    dq = deque(range(1, N + 1))   # 덱으로 1 ~ N + 1까지 번호매겨 deque에 추가

    while len(dq) > 1:   # 최후의 번호가 남을 때까지 반복
        for i in range(K - 1):   # k 번째가 가장 앞으로 오도록
            dq.append(dq.popleft())   # 위 주석 내용에 포함되는 라인
            dq.popleft()   # k번째 요소 삭제

    return dq[0]   # 마지막 요소 return

print(solution(5, 2))