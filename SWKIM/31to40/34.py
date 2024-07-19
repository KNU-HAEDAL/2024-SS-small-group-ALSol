def solution(nums):
    answer = 0
    size = len(nums) // 2
    pokemon = set(nums)
    
    # 포켓몬의 종류와 nums 절반의 수 비교
    # 그 중 작은 값을 선택해 반환
    if size > len(pokemon):
        answer = len(pokemon)
    else:
        answer = size

    return answer

nums = [3,1,2,3]
print(solution(nums))