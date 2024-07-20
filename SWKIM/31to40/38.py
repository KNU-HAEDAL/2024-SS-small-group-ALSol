# 깊이 우선 탐색
def dfs(graph_dict, visited, start):
    visited.append(start)

    # key가 존재한다면
    if start in graph_dict:
        # 방문하지 않은 곳을 추가하고 재귀적으로 실행
        for cur in graph_dict[start]:
            if cur not in visited:
                dfs(graph_dict, visited, cur)

def solution(graph, start):
    graph_dict = {}
    visited = []
    
    # dict으로 그래프 형성
    for u, v in graph:
        if u not in graph_dict:
            graph_dict[u] = []
            graph_dict[u].append(v)
        else:
            graph_dict[u].append(v)

    dfs(graph_dict, visited, start)
    
    return visited

graph = [['A', 'B'], ['A', 'C'], ['B', 'D'], ['B', 'E'], ['C', 'F'], ['E', 'F']]
start = 'A'
print(solution(graph, start))