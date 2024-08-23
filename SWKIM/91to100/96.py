from collections import deque
def solution(queue1, queue2):
    answer = 0

    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    size = len(queue1)
    score1 = sum(queue1)
    score2 = sum(queue2)   

    # 두 큐의 합이 홀수인 경우
    if (sum(queue1) + sum(queue2)) % 2 == 1:
        return -1
    
    while True:
        # 계속 반복해도 같아질 수 없는 경우
        if answer > size*3:
            return -1
        
        # 같은 경우
        if score1 == score2:
            break

        # 합이 큰 쪽이 작은 쪽으로 이동
        if score1 > score2:
            n = queue1.popleft()
            score1 -= n
            score2 += n
            queue2.append(n)
        else:
            n = queue2.popleft()
            score2 -= n
            score1 += n
            queue1.append(n)

        answer += 1

    return answer



print(solution([3, 2, 7, 2], [4,6,5,1]))