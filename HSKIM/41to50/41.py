def solution(graph, source):
    v = len(graph)
    distance = [float("inf") for _ in range(v)]
    predecessor = [None for _ in range(v)]
    distance[source] = 0

    # 정점 개수(V - 1) 만큼 반복
    for i in range(v - 1):
        for node in range(v):
            for neighbor, weight in graph[node]:
                # 현재 정점을 거쳐 가는 거리가 더 작은 경우
                if distance[neighbor] > distance[node] + weight:
                    distance[neighbor] = distance[node] + weight
                    # 거쳐온 이전 노드 저장
                    predecessor[neighbor] = node
    
    # 음수 사이클 존재 여부 확인
    for node in range(v):
        for neighbor, weight in graph[node]:
            if distance[neighbor] > distance[node] + weight:
                return [-1]  # 음수 사이클이 존재하면 -1 반환
    
    return [distance, predecessor]

# 그래프 정의: 인접 리스트 (정점, 가중치)
graph = [
    [(1, 5), (2, -1)],  # 0번 정점에서 1번 정점으로 가중치 5, 2번 정점으로 가중치 -1
    [(2, 2)],          # 1번 정점에서 2번 정점으로 가중치 2
    [(3, -2)],         # 2번 정점에서 3번 정점으로 가중치 -2
    [(0, 2), (1, 6)]   # 3번 정점에서 0번 정점으로 가중치 2, 1번 정점으로 가중치 6
]

source = 0
print(solution(graph, source))
