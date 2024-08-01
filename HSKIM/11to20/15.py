def solution(N, K):
    queue = list(range(1, N + 1))
    
    # 시작 인덱스
    index = 0  

    while len(queue) > 1:
        # K번째 요소를 찾기 위해 index를 이동
        index = (index + K - 1) % len(queue)
        # K번째 요소 제거
        queue.pop(index)
    
    return queue[0]  

