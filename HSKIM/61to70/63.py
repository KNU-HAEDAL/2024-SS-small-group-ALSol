def solution(matrix1, matrix2):
    # 두 행렬 곱하기
    size = len(matrix1)
    multiplied_matrix = [[0] * size for _ in range(size)]

    for i in range(size):
        for j in range(size):
            for k in range(size):
                multiplied_matrix[i][j] += matrix1[i][k] * matrix2[k][j]
    # 주어진 행렬의 전치 행렬을 반환
    return [[multiplied_matrix[j][i] for j in range(len(multiplied_matrix))] for i in range(len(multiplied_matrix[0]))]

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

print(solution(matrix1, matrix2))
# 예상 결과: [[30, 84, 138], [24, 69, 114], [18, 54, 90]]
