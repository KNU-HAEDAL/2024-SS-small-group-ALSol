arr1 = ([[1, 4], [3, 2], [4, 1]])
arr2 = ([[3, 3], [3, 3]])

arr3 = ([[2, 3, 2], [4, 2, 4], [3, 1, 4]])
arr4 = ([[5, 4, 3], [2, 4, 1], [3, 1, 1]])


#len(arr1) = 3
#len(arr1[1]) = 2


def solution(arr_1, arr_2):
    res = [[0] * len(arr_2) for _ in range(len(arr_1))]
    for i in range(len(arr_1)):
        for j in range(len(arr_1)):
            for k in range(len(arr_2)):
                res[i][j] += arr_1[i][k] * arr_2[k][j]
    return res

print(solution(arr1, arr2))
print(solution(arr3, arr4))     

# (3X2) X (2X2) 행렬 = (3X2)