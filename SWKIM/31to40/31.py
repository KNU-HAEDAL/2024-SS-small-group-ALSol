from collections import deque

def solution(info, edges):
    answer = 0
    queue = deque()

    tree = {x: [] for x in range(len(info))} # key: 부모 노드, value: 자식 노드
    # 트리 생성
    for i in edges:
        tree[i[0]].append(i[1])
    
    queue.append([0, 1, 0, set()]) # index, 양, 늑대, 방문 가능한 노드 집합
    
    while True:
        if len(queue) == 0:
            break
        
        cur, sheep, wolf, visited = queue.popleft()
        
        visited.update(tree[cur]) # 현재 노드의 자식 노드를 방문 가능한 노드 집합에 추가
        
        answer = max(sheep, answer) # 양의 수가 최대인 값을 가짐

        # 방문 가능한 노드 중 늑대의 수가 양의 수보다 같아지지 않다면 큐에 추가
        for i in visited:
            if info[i] == 0:    # 양인 경우
                temp = visited.copy()
                temp.remove(i)  # 현재 노드를 삭제함으로 중복 방문 막기
                queue.append([i, sheep+1, wolf, temp])
            elif sheep != wolf + 1: # 늑대인 경우 늑대가 양보다 같아지지 않는다면 
                temp = visited.copy()
                temp.remove(i)
                queue.append([i, sheep, wolf+1, temp])


    return answer


info = [0,0,1,1,1,0,1,0,1,0,1,1]
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]

print(solution(info, edges))

