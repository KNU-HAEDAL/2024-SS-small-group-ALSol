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


##### defaultdict
# 일반적인 파이썬 딕셔너리는 키가 존재하지 않을 때 KeyError를 발생시킨다.
# defaultdict는 기본값을 자동으로 생성, 키가 존재하지 않을 경우에도 예외를 발생시키지 않고 기본값을 제공할 수 있다.

# defaultdict(int)는 기본값으로 0을 설정한다.
# defaultdict(list)는 기본값으로 빈 리스트 []를 설정한다.

# 그래프를 구성할 때 노드가 이미 존재하는지 확인할 필요 없이, 새로운 연결을 추가할 수 있다.