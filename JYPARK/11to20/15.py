from collections import deque
def solution(N, K):
    queue = deque(range(1, N+1))
    while True:
        for i in range(K-1):
            queue.append(queue.popleft())
            queue.popleft()
        if len(queue) == 1:
            answer = queue.popleft()
            break
    return answer
        

N = 5
K = 2
print(solution(N, K))