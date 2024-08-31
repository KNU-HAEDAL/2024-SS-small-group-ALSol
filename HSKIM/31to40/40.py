from collections import deque

def soluiton(graph, start):
    graph_dict = {x: 0 for x in graph}  # 최소 거리를 가리키는 dict
    paths = {x: [] for x in graph}  # 최소 거리까지 거치는 경로를 가리키는 dict
    paths[start].append(start) # start 노드는 자기 자신이 도착지이기 때문에 우선적으로 처리

    queue = deque() # 너비 우선 탐색을 하기 위한 큐

    # 각 노드당 최소거리와 경로를 찾기 위한 for문
    for i in graph:
        # 시작 노드 제외
        if i == start:
            continue
        
        # 출발 노드, 거리, 경로를 큐에 추가
        queue.append([start, 0, [start]])        
        weight = -1 # 초기화

        while queue:
            cur, cnt, path = queue.popleft()
            
            # 현재 노드가 도착지라면
            if cur == i:
                # 거리 비교를 통해 더 작은 거리 저장
                if weight != -1:
                    weight = min(weight, cnt)
                else:
                    weight = cnt
                
                # 최소 거리가 수정됬다면 거리 수정
                if weight == cnt:
                    paths[i] = path
            # 현재 노드가 도착지가 아니라면
            else:
                # 거리가 최소 거리보다 크면 생략
                if weight != -1 and cnt > weight:
                    continue
                # 거리 수정 및 경로에 다음 도착지를 추가하고 큐에 추가
                for next in graph[cur]:
                    copy_path = path.copy()
                    copy_path.append(next)
                    queue.append([next, cnt+graph[cur][next], copy_path])
        
        graph_dict[i] = weight

    return [graph_dict, paths]

graph = {
    'A': {'B': 1},
    'B': {'C': 5},
    'C': {'D': 1},
    'D':{}
}

start = 'A'
print(soluiton(graph, start))