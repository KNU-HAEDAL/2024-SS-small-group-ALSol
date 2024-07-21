from collections import defaultdict

def solution(graph, start):
    distance = defaultdict(int)
    path = defaultdict(list)
    
    for i in graph.keys():
        cur = start
        while True:
            if cur == i:
                distance[cur]
                path[cur].append(cur)
                break
    return 


graph = {
    'A': {'B': 9, 'C': 3},
    'B': {'A': 5},
    'C': {'B':1}
}
start = 'A'

print(solution(graph, start))