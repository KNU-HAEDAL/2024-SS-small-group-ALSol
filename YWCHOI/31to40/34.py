def solution(nums):
    numbers = set(nums)
    select = len(nums) // 2

    if select >= numbers :
        return numbers
    else :
        return select