def solution(nums):
    L = len(nums)//2             #가질 수 있는 폰겟몬 수
    s = set(nums)
    if len(s) <= L:
        return len(s)
    else:
        return L

nums = [3, 1, 2, 3] 
print(solution(nums))