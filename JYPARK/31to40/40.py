import heapq                #heapq 모듈은 이진 트리 기반의 최소 힙 자료구조를 제공함
def solution(graph, start):
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    q = []                  #큐(최소힙)
    heapq.heappush(q, [distances[start], start])
    paths = {start: [start]}

    while q:
        current_distance, current_node = q.pop()

        if current_distance > distances[current_node]:
            continue
        
        for adjacent_node, weight in graph[current_node].items():
            if current_distance + weight < distances[adjacent_node]:
                distances[adjacent_node] = current_distance + weight
                heapq.heappush(q, [current_distance + weight, adjacent_node])
                paths[adjacent_node] = paths[current_node] + [adjacent_node]

    return [distances, paths]

#graph = { 'A': {'B': 9, 'C': 3}, 'B': {'A': 5}, 'C': {'B': 1} }
graph = {'A': {'B': 1},'B': {'C': 5},'C': {'D': 1},'D': { } }
start = 'A'
print(solution(graph, start))