from collections import Counter
# union-find를 이용하여 서로 다른 트리의 노드 수 비교
def find(nodes, u):
    if nodes[u] == u:
        return u
    
    nodes[u] = find(nodes, nodes[u])
    return nodes[u]

def union(nodes, u, v):
    root1 = find(nodes, u)
    root2 = find(nodes, v)

    if root1 != root2:
        if root1 < root2:
            nodes[root2] = root1
        else: 
            nodes[root1] = root2

def solution(n, wires):
    original_nodes = [x for x in range(n+1)]
    
    answer = []

    # wires에서 각 하나씩 빼고 트리를 구성하여 노드 수 비교
    for i in range(len(wires)):
        nodes = original_nodes.copy()
        for j in range(len(wires)):
            if j == i:  # 하나씩 제외
                continue
            u, v = wires[j]

            union(nodes, u, v)
        
        # 생성한 트리의 노드 수를 비교하여 그 값을 answer에 저장
        result = [find(nodes, x) for x in range(n+1)]
        result.pop(0)
        result = Counter(result)
        print(result)
        if len(result) == 2:
            result = result.values() 
            answer.append(max(result) - min(result))

    # answer에 저장된 두 트리의 차의 최솟값을 반환
    return min(answer)

print(solution(9 ,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
            


