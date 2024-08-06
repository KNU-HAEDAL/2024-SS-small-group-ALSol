def union(x, y, parents):
    root1 = find(x, parents)
    root2 = find(y, parents)
    parent = max(root1, root2)
    child = min(root1, root2)
    parents[child] = parent             #더 큰 수를 부모노드를 설정함.

#루트노드 찾는 메서드
def find(x, parents):
    if parents[x] == x:                     #루트노드인 경우
        return x
    return find(parents[x], parents)

def solution(n, costs):
    edges = 0
    answer = 0
    parents = [i for i in range(n)]
    costs.sort(key = lambda x:x[2])         #비용기준 오름차순 정렬

    for i in range(len(costs)):
        if edges == n-1:                    #간선이 n-1개 연결되면 모든 노드들이 연결된 것임.
            break
        
        if find(costs[i][0], parents) != find(costs[i][1], parents):        #두 노드의 루트 노드가 같지 않다면(=사이클이 형성되지 않음)
            edges += 1
            answer += costs[i][2]
            union(costs[i][0], costs[i][1], parents)
    return answer

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
print(solution(n, costs))