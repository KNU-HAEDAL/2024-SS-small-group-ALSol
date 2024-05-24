def solution(arr1, arr2):
    row1 = len(arr1)
    col1 = len(arr1[0])

    row2 = len(arr2)
    col2 = len(arr2[0])

    arr3 = [[0] * col2 for _ in range(row1)]
    
    for i in range(row1):
        for j in range(col2):
            for k in range(col1):
                arr3[i][j] += arr1[i][k] * arr2[k][j]
    
    return arr3

a1 = [[2, 3, 2], [4, 2, 4], [3,1, 4]]
a2 = [[5, 4, 3], [2, 4,1], [3,1,1]]

print(solution(a1, a2))
