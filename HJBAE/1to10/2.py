arr1 = [4, 2, 2, 1, 3, 4]
arr2 = [2, 1, 1, 3, 2, 5, 4]

def sol(arr):
    del_arr = list(set(arr))
    del_arr.sort(reverse = True)
    return del_arr

print(sol(arr1))
print(sol(arr2))

