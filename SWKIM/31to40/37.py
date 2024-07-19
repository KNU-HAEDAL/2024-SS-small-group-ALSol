# 루트 노드 찾기
def find(nodes, x):
    if nodes[x] == x:
        return x
    
    root = find(nodes, nodes[x])
    return root

# 두 노드 이어주기
def union(nodes, x, y):
    root1 = find(nodes, x)
    root2 = find(nodes, y)
    
    # 루트 노드 비교(사이클 확인 용도)
    if root1 != root2:  # 사이클이 형성되지 않는다면
        nodes[root2] = root1

        return True
    
    # 사이클 형성
    return False

def solution(n, costs):
    answer = 0
    nodes = [i for i in range(n)]
    # cost 기준으로 오름차순 정렬
    sorted_costs = sorted(costs, key= lambda x: x[2])
    
    # 사이클 형성이 아니라면 총합에 cost 더하기
    for x, y, cost in sorted_costs:
        if union(nodes, x, y):
            answer += cost
    
    return answer

print(solution(4, [[0,1,1],[0,2,3],[1,2,2],[1,3,1],[2,3,8]]))