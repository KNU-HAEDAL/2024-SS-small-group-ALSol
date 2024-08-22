from collections import deque

def solution(info, edges):
    def build_tree(info, edges):
        tree = [[] for _ in range(len(info))]
        for edge in edges:
            tree[edge[0]].append(edge[1])
        return tree
    
    tree = build_tree(info, edges) # 트리 생성
    max_sheep = 0

    q = deque([(0, 1, 0, set())])

    # BFS
    while q:
        cur, sheep_cnt, wolf_cnt, visited = q.popleft()
        max_sheep = max(max_sheep, sheep_cnt)
        # 기존 딕셔너리에 새로운 키-값 쌍을 추가하거나, 이미 존재하는 키의 값을 업데이트하는 데 사용됨
        visited.update(tree[cur])

        # 인접한 노드들에 대해 탐색
        for next_node in visited:
            if info[next_node]: # 늑대일 경우
                if sheep_cnt != wolf_cnt + 1:
                    q.append(
                        (next_node, sheep_cnt, wolf_cnt + 1, visited - {next_node})
                    )
            else: # 양일 경우
                q.append(
                    (next_node, sheep_cnt + 1, wolf_cnt, visited - {next_node})
                )

    return max_sheep

info = [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1]
edges = [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9,10], [9,11], [4, 3], [6, 5], [4, 6], [8, 9]]

print(solution(info, edges))