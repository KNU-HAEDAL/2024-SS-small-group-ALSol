def solution(graph, source):
    size = len(graph)
    dist = [float("inf") for _ in range(size)]
    dist[source] = 0
    adjacent_node = [None for _ in range(size)]
    
    for i in range(size - 1):       #노드개수 - 1 만큼 반복
        for current_node in range(size):        
            for node, weight in graph[current_node]:        #graph[curr]은 curr에서 출발하는 간선들의 리스트
                if dist[current_node] + weight < dist[node]:
                    dist[node] = dist[current_node] + weight
                    adjacent_node[node] = current_node

    #음의 가중치 순회가 있는지 확인
    for current_node in range(size):
        for node, weight in graph[current_node]:
            if dist[current_node] + weight < dist[node]:        #최소 비용이 갱신되는 노드가 있다면 음의 순회가 존재하는 것.
                return [-1]
            
    return [dist, adjacent_node]
    
graph = [[(1, 4), (2, 3), (4, -6 )], [(3, 5)], [(1, 2)], [(0, 7), (2, 4)],[(2, 2)]]
#graph = [[(1, 5), (2, -1)], [(2, 2)], [(3, -2)], [(0, 2), (1, 6)]]
source = 0
print(solution(graph, source))