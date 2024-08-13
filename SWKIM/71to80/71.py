def solution(nums):
    n = len(nums)
    dp = [1]*n

    # nums의 각 숫자와 그 앞의 숫자를 비교
    for i in range(n):
        for j in range(i):
            # i번째 수가 그 앞의 수보다 크다면
            if nums[i] > nums[j]:
                # 만들 수 있는 수열 중 최댓값을 저장
                dp[i] = max(dp[i], dp[j]+1)

    return max(dp)  # 최댓값 반환

print(solution([1,3,2,3,1,5,7,3])) 