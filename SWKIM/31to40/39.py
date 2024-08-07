from collections import defaultdict
from collections import deque

# 너비 우선 탐색 알고리즘
def bfs(graph_dict, start):
    result = []
    queue = deque()
    result.append(start)
    queue.append(start)

    # 큐를 통해 깊이 우선이 아닌 너비 우선으로 탐색
    while len(queue) > 0:
        cur = queue.popleft()

        # 방문하지 않는 노드라면 큐에 추가
        for i in graph_dict[cur]:
            if i not in result:
                result.append(i)
                queue.append(i)
    
    return result

def solution(graph, start):
    graph_dict = defaultdict(list)

    for u, v in graph:
        graph_dict[u].append(v)
    
    answer = bfs(graph_dict, start)

    return answer

graph = [(0,1), (1, 2), (2, 3), (3, 4),(4, 5),(5, 0)]
start = 1
print(solution(graph, start))