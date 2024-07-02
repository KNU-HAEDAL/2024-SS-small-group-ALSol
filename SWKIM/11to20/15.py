from collections import deque

def solution(N, K):
    queue = deque()

    # 큐에 1부터 n까지 수 추가
    for i in range(N):
        queue.append(i+1)
    
    
    while(len(queue) > 1):
        # k번째 숫자 찾기
        for _ in range(K-1):
            data = queue.popleft()
            queue.append(data)
        
        # k번쨰 숫자 제거
        queue.popleft()
    
    return queue.popleft()

print(solution(5, 2)) 