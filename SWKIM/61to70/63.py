def solution(matrix1, matrix2):
    # 행렬 곱
    def multi(matrix1, matrix2):
        matrix3 = [[0 for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    matrix3[i][j] += matrix1[i][k] * matrix2[k][j]
        
        return matrix3
    
    answer = multi(matrix1, matrix2)
    
    # 전치    
    for i in range(3):
        for j in range(i, 3):
            temp = answer[i][j]
            answer[i][j] = answer[j][i]
            answer[j][i] = temp
    
    return answer

matrix1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
matrix2 = [
    [9,8,7],
    [6,5,4],
    [3,2,1]
]
print(solution(matrix1, matrix2))