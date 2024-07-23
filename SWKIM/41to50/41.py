def solution(graph, source):
    size = len(graph)
    distance = [float("inf") for _ in range(size)]
    distance[source] = 0    # 시작 노드의 거리를 0으로 초기화
    predecessor = [None for _ in range(size)]

    # 최솟값 구하기
    for i in range(size - 1): # V - 1만큼 실행
        for cur in range(size): # 각 노드를 모두 방문
            for node, weight in graph[cur]: # 현재 노드에서 갈 수 있는 노드들
                # 거리 비교를 통해 이동할 때의 거리가 더 짧다면 거리 수정
                if distance[cur] + weight < distance[node]:
                    distance[node] = distance[cur] + weight
                    predecessor[node] = cur
    
    # 음의 가중치 순회가 있는지 확인
    for cur in range(size):
            for node, weight in graph[cur]:
                if distance[cur] + weight < distance[node]:
                    return [-1]
                
    return [distance, predecessor]    

graph = [[(1, 5), (2, -1)], [(2, 2)], [(3, -2)], [(0, 2), (1, 6)]]
source = 0
print(solution(graph, source))