import heapq

def solution(N, road, K):
    answer = 0
    dist = {i+1: float("inf") for i in range(N)}
    dist[1] = 0
    q = []
    graph = [[]for _ in range(N+1)]    

    for i, j, weight in road:
        graph[i].append((j, weight))
        graph[j].append((i, weight))

    heapq.heappush(q, [0, 1])          #시작점에서 현재노드까지의 거리, 현재노드    !heapq를 사용한 이유 -> 방문하지 않은 노드들 중 최소거리를 가지는 노드를 선택해야하므로 거리값을 튜플의 첫 번째 요소(정렬기준)로 사용해야한다.

    while q:
        weight, current_node = heapq.heappop(q)
        
        for adjacent_node, new_weigth in graph[current_node]:                 #현재노드에 연결 돼있는 모든 노드를 볼 것임
            if dist[adjacent_node] > dist[current_node] + new_weigth:
                dist[adjacent_node] = dist[current_node] + new_weigth
                heapq.heappush(q, [dist[adjacent_node], adjacent_node])
                
    for key in dist:
        if dist[key] <= K:
            answer += 1
    return answer
   
#N, road, K = 5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3
N, road, K = 6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4
print(solution(N, road, K))