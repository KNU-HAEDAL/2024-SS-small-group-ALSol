# 1번 번호표를 가진 사람을 기준으로 K번째 사람을 없앰
# 없앤 사람 다음 사람을 기준으로 하고 다시 K번째 사람을 없앰

from collections import deque

def solution(N, K):
    queue = deque(range(1, N + 1))

    while (len(queue) > 1):
        for i in range(K - 1):
            queue.append(queue.popleft())
            queue.popleft()
    return queue[0]

print(solution(5, 2))    

"""
12345

12345    2 pop(popleft) 1 push(popleft + append) 
3451    4 pop 3 push
513    1 pop 5 push
35   5 pop 3 push
3    3 left

1트 while ((len(queue) == 1)is True) 하니까 1 나옴
2트 while (len(queue) == 1) ㅋㅋ 암튼 1 나옴
아 이거 그냥 내가 바보였음
"""