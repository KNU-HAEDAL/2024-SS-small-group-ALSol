arr1 = [2, 1, 3, 4, 1]
arr2 = [5, 0, 2, 7]

def sum_arr(arr):
    res = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            res.append(arr[i] + arr[j])
    res = sorted(set(res))
    return res

print(sum_arr(arr1))
print(sum_arr(arr2))