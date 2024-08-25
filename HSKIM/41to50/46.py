def dfs(graph, node, visited):
    count = 1  # 현재 노드부터 시작하므로 초기값 1
    visited[node] = True
    
    for neighbor in graph[node]:
        if not visited[neighbor]:
            count += dfs(graph, neighbor, visited)
    
    return count

def solution(n, wires):
    answer = float('inf')
    
    # 인접 리스트로 그래프 표현
    for i in range(len(wires)):
        # 전선을 하나 제거하여 그래프 생성
        graph = {i: [] for i in range(1, n + 1)}
        for j in range(len(wires)):
            if i == j:
                continue
            u, v = wires[j]
            graph[u].append(v)
            graph[v].append(u)
        
        # 방문 체크용 리스트
        visited = [False] * (n + 1)
        
        # 임의의 노드에서 DFS를 시작하여 하나의 트리의 크기를 계산
        first_tree_size = dfs(graph, 1, visited)
        
        # 다른 트리의 크기는 전체 노드 수에서 첫 번째 트리의 크기를 빼면 됨
        second_tree_size = n - first_tree_size
        
        # 두 트리 크기의 차이의 최솟값을 갱신
        answer = min(answer, abs(first_tree_size - second_tree_size))
    
    return answer

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))  # 예상 결과: 3
