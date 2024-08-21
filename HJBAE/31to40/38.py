"""
깊이 우선 탐색으로 모든 그래프의 노드를 순회하는 함수 solution()을 작성
시작 노드는 Start
graph는 [출발 노드, 도착 노드] 쌍들이 들어있는 리스트
반환값은 그래프의 시작 노드부터 모든 노드를 깊이 우선 탐색으로 진행한 순서대로 노드가 저장된 리스트
"""

# 그래프 -> 인접 리스트 변환
def solution(graph, start):
    # 인접 리스트 -> 키 : 출발 노드, 값 : 연결된 노드
    adj_list = {}
    for edge in graph:
        # 출발 노드가 아직 추가 전이면 빈 리스트 초기화
        if edge[0] not in adj_list:
            adj_list[edge[0]] = []
        if edge[1] not in adj_list:
            adj_list[edge[1]] = []
        # 출발 노드에 도착 노드를 추가 -> 그래프를 인접 리스트 형태로 저장
        adj_list[edge[0]].append(edge[1])

    # 방문한 노드 중복 안되게
    visited = set()
    # 순서 기록
    result = []

    # DFS 함수
    def dfs(node):
        if node not in visited:
            # 방문 안했으면 방문한거 추가하고 순서 기록
            visited.add(node)
            result.append(node)
            # 인접 노드 재귀로 반복 -> 다시 위로 ㅋㅋ
            for neighbor in adj_list[node]:
                dfs(neighbor)
    
    # 시작 노드부터..
    dfs(start)
    return result

graph1 = [['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E']]
start = 'A'
# return1 = ['A', 'B', 'C', 'D', 'E']

graph2 = [['A', 'B'], ['A', 'C'], ['B', 'D'], ['B', 'E'], ['C', 'F'], ['E', 'F']]
# return2 = ['A', 'B', 'D', 'E', 'F', 'C']

print(solution(graph1, start))
print(solution(graph2, start))

# 아 헷갈린다