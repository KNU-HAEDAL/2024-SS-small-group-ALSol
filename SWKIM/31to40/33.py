# 집합 합치기
def union(arr, x, y):
    #루트 계산
    root1 = find(arr, x)
    root2 = find(arr, y)

    arr[root2] = root1
    return

# 루트 찾기
def find(arr, x):
    child = x
    parent = arr[child]

    # 배열의 값이 본인 idx이면 break
    while True:
        if parent == arr[child]:
            break
        
        child = parent
        parent = arr[child]

    return parent

def solution(k, operations):
    arr = [i for i in range(k)]
    answer = 0

    for operation in operations:
        op = operation[0]

        if op == 'u':
            union(arr, operation[1], operation[2])
        elif op == 'f':
            find(arr, operation[1])

    # 서로 다른 root의 갯수를 반환
    answer = len(set(find(arr, i) for i in range(k)))
    return answer

k = 4
operations = [['u',0,1], ['u', 2,3], ['f', 0]]
print(solution(k, operations))