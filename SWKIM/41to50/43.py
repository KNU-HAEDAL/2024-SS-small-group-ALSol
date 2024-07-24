from collections import deque

def solution(n, computers):
    visited = [True for _ in range(n)]
    queue = deque()
    answer = set()

    for comp in range(n):
        # 아직 방문하지 않은 컴퓨터라면 방문한다.
        if visited[comp]:
            visited[comp] = False
            queue.append(comp)

            # 해당 컴퓨터와 이어진 다른 컴퓨터를 모두 찾을 때까지 반복
            while queue:
                cur = queue.popleft()

                # 이어진 컴퓨터가 방문하지 않은 컴퓨터면 큐에 저장
                for i in range(n):
                    if computers[cur][i] == 1 and visited[i]:
                        queue.append(i)
                        visited[i] = False
            
            # 처음 출발한 컴퓨터를 집합에 저장 
            answer.add(comp)
    
    # 집합에 저장된 컴퓨터의 수 반환
    return len(answer)

n = 3
computer = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n, computer))

    
    


