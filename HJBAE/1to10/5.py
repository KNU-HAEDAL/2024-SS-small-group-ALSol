import numpy as np

arr1 = np.array([[1, 4], [3, 2], [4, 1]])
arr2 = np.array([[3, 3], [3, 3]])
# 추가로 제시된 행렬은.. arr3, arr4로 해서 돌려봄

arr3 = np.array([[2, 3, 2], [4, 2, 4], [3, 1, 4]])
arr4 = np.array([[5, 4, 3], [2, 4, 1], [3, 1, 1]])

def sol(arr1, arr2):
    res = np.dot(arr1, arr2)
    return res

print(sol(arr1, arr2))
print(sol(arr3, arr4))