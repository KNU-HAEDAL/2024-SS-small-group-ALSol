def solution(arr):
    newArr = list(set(arr))
    newArr.sort(reverse=True) # 내림차순 정렬
    return newArr

nums = [4, 2, 2, 1, 3, 4]
print(solution(nums))