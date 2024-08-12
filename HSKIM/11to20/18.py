def solution(arr, target):
    l = len(arr)
    for i in range(0, l-1):
        for j in range(i + 1, l): 
            print(arr[i] + arr[j], target)
            if (arr[i] + arr[j]) == target:
                return True
    return False

# print(solution([1,2,3,4,8], 6))
# print(solution([2,3,5,9], 10))
