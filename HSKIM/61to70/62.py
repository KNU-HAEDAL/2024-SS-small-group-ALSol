def rotate_90_degrees(arr):
    # 2차원 배열을 시계 방향으로 90도 회전
    size = len(arr)
    rotated = [[0] * size for _ in range(size)]

    for i in range(size):
        for j in range(size):
            rotated[j][size - 1 - i] = arr[i][j]

    return rotated

def solution(arr, n):
    for _ in range(n):
        arr = rotate_90_degrees(arr)
    return arr

arr = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
n = 1
print(solution(arr, n))  

n = 2
print(solution(arr, n))  
