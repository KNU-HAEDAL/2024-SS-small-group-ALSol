"""
상호배타적 집합을 표현하고 관리하는 데 다음 두 연산 필요
union(x, y) : x와 y가 속한 두 집합을 합침
find(x, y) : x가 속한 집합의 대표 원소를 찾음
operations 라는 배열은 수행할 연산을 의미 -> 연산 종류는 2개
['u', 1, 2] 는 노드 1과 노드 2에 대해 union 연산 수행
['f', 3] 노드 3의 루트 노드 찾기, find 연산 수행
초기의 노드는 부모 노드를 자신의 값으로 설정했다고 가정 -> 여기서는 각 집합의 루트 노드를 기준으로 루트 노드가 작은 노드를 더 큰 노드의 자식으로 연결하는 방법을 사용
operations에 있는 연산을 모두 수행한 후 집합의 개수를 반환하는 solution() 함수 구현
"""
def operation_find(pre_list, x):    # 이게 !!루트 노드!! 찾는 함수
    if pre_list[x] == x:
        return x
    pre_list[x] = operation_find(pre_list, pre_list[x])
    return pre_list[x]

def operation_union(pre_list, rank, x, y):
    rootX = operation_find(pre_list, x)
    rootY = operation_find(pre_list, y)

    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            pre_list[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            pre_list[rootX] = rootY
        else:
            pre_list[rootY] = rootX
            rank[rootX] += 1

def solution(k, operations):
    # solution 함수 이전에 전체 노드 배열 만들고, union 연산이랑 find 연산 함수도 만들어야 함
    for i in range(k):
        pre_list = list(range(k))    # 모든 항이 자기 인덱스
    rank = [0] * k
    
    for oper in operations:
        if oper[0] == 'u':    # ['u', 1, 2] 는 노드 1과 노드 2에 대해 union 연산 수행
            oper1 = oper[1]
            oper2 = oper[2]
            operation_union(pre_list, rank, oper1, oper2)
        elif oper[0] == 'f':    # ['f', 3] 노드 3의 루트 노드 찾기, find 연산 수행 
            operation_find(pre_list, oper[1])
        
    root_set = set()
    for i in range(k):
        root_set.add(operation_find(pre_list, i))
    
    return len(root_set)

k1 = 3
operations1 = [['u', 0, 1], ['u', 1, 2], ['f', 2]]
# result1 = 1
k2 = 4
operations2 = [['u', 0, 1], ['u', 2, 3], ['f', 0]]
# result2 = 2
print(solution(k1, operations1))
print(solution(k2, operations2))