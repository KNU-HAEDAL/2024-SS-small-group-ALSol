arr1 = ([[1, 4], [3, 2], [4, 1]])
arr2 = ([[3, 3], [3, 3]])

arr3 = ([[2, 3, 2], [4, 2, 4], [3, 1, 4]])
arr4 = ([[5, 4, 3], [2, 4, 1], [3, 1, 1]])

def solution(arr_1, arr_2):
    row1, column1 = len(arr_1), len(arr_1[0])
    row2, column2 = len(arr_2), len(arr_2[0])

    res = [[0] * len(arr_1)] * len(arr_2[0])

    for i in range(len(arr_1)):    # len(arr_1) == len(row1)
        for j in range(len(arr_2[0])):    # len(arr_1) == len(column1)
            for k in range(len(arr_1[0])):    # len(arr_2) == len(column2)
                res[i][j] += arr_1[i][k] * arr_2[k][j]
    
    return res


print(solution(arr1, arr2))
print(solution(arr3, arr4))



