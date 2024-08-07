from collections import defaultdict, deque

def solution(graph, start):
    tree = defaultdict(list)
    visited = set()
    answer = []
    for i, j in graph:
        tree[i].append(j)
    return bfs(tree, start, visited, answer)

def bfs(tree, node, visited, answer):
    q = deque()
    q.append(node)

    while q:
        node = q.popleft()
        if node not in visited:
            visited.add(node)
            answer.append(node)        
            q.extend(tree[node])
    return answer

#graph = [(1, 2), (1, 3), (2, 4), (2, 5),(3, 6),(3, 7),(4, 8), (5, 8),(6, 9),(7, 9)]
graph = [(0,1), (1, 2), (2, 3), (3, 4),(4, 5),(5, 0)] 
start = 1
print(solution(graph, start))