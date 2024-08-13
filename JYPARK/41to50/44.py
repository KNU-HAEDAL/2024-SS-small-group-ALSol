import heapq
from collections import defaultdict

def solution(N, road, K):
    answer = 0
    visited = [False for _ in range(N)]
    visited[0] = True
    dist = {i+1: float("inf") for i in range(N)}
    dist[1] = 0
    q = []
    graph = [[]for _ in range(N+1)]    

    for current_node, adjacent_node, weight in road:
        graph[current_node].append((adjacent_node, weight))
        graph[adjacent_node].append((current_node, weight))

    heapq.heappush(q, [1, 0])          #현재노드, 시작점에서 현재노드까지의 거리

    while q:
        current_node, weight = heapq.heappop(q)
        
        if dist[current_node] < weight:
            continue
        
        for adjacent_node, new_weigth in graph[current_node]:                 #현재노드에 연결 돼있는 모든 노드를 볼 것임
            if dist[adjacent_node] > dist[current_node] + new_weigth:
                dist[adjacent_node] = dist[current_node] + new_weigth
                heapq.heappush(q, [adjacent_node, dist[adjacent_node]])
                
    for key in dist:
        if dist[key] <= K:
            answer += 1
    return answer
   
#N, road, K = 5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3
N, road, K = 6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4
print(solution(N, road, K))