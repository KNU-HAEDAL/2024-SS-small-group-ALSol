def find(x, parents):
    if parents[x] == x:
        return x
    find(parents[x], parents)
    
def union(x, y, parents):
    #각 원소가 속한 집합의 루트노드 찾기
    root1 = find(x, parents)
    root2 = find(y, parents)
    
    #두개의 루트노드 크기 비교
    if root1 > root2:
        parent = root1
        child = root2
    else:
        parent = root2
        child = root1
    parents[child] = parent

def solution(k, operations):
    answer = 0
    parents = [i for i in range(k)]
    
    for i in range(len(operations)):
        if operations[i][0] == 'u':
            union(operations[i][1], operations[i][2], parents)
        else:
            find(operations[i][1], parents)

    for j in range(len(parents)):
        if parents[j] == j:                 #루트노드의 개수 세기
            answer += 1
    return answer

k = 3
operations = [['u', 0, 1], ['u', 1, 2], ['f', 2]]
#k = 4
#operations = [['u', 0, 1],['u', 2, 3], ['f', 0]]
print(solution(k, operations))