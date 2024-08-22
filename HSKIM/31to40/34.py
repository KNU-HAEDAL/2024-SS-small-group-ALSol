def solution(nums):
    answer = 0
    size = len(nums) // 2
    pokemon = set(nums)

    answer = min(size, len(pokemon))

    return answer

nums = [3,1,2,3]
print(solution(nums))