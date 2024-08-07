#깊이 우선 탐색
from collections import defaultdict

def solution(graph, start):
    answer = []
    tree = defaultdict(list)
    visited = set()

    #그래프를 인접 리스트로 변환
    for node in graph:
        tree[node[0]].append(node[1])
    
    return dfs(tree, start, visited, answer)
    
def dfs(tree, node, visited, answer):
    visited.add(node)
    answer.append(node)
    for i in tree.get(node, []):                #node가 tree에 존재하지 않을경우, []를 반환함
        if i not in visited:                    #방문한 노드가 아니라면
            dfs(tree, i, visited, answer)
    return answer

#graph = [['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E']]
graph = [['A', 'B'], ['A', 'C'], ['B', 'D'], ['B', 'E'], ['C', 'F'], ['E', 'F']]
start = 'A'
print(solution(graph, start))