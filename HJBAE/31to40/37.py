"""
n개의 섬 사이에 다리를 건설하는 비용 costs가 주어질 때
최소 비용으로 모든 섬이 서로 통행하는 solution() 함수
다리를 여러 번 건너더라도 목표 지점에 도달할 수만 있으면 통행할 수 있다고 봄
A, B 섬 사이에 다리가 있고, B, C 섬 사이에 다리가 있으면 A, C 섬은 서로 통행할 수 있음
"""
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)

    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1
        
def solution(n, costs):
    # 부모와 rank 초기화
    parent = [i for i in range(n)]
    rank = [0] * n

    costs.sort(key = lambda x : x[2])

    mst_cost = 0
    edges_used = 0

    for u, v, cost in costs:
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            mst_cost += cost
            edges_used += 1
            if edges_used == n - 1:
                break
    
    return mst_cost

n = 4
costs = [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]
# return = 4
print(solution(n, costs))