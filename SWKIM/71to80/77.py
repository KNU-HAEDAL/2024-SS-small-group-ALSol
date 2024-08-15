def solution(money):    
    n = len(money)

    # 첫 집을 훔친 경우와 아닌 경우를 구분 및 초기화
    dp = [[0]*n for _ in range(2)]
    dp[0][0], dp[0][1] = money[0], money[0]
    dp[1][1] = money[1]

    # 이전 dp 값과 그 이전의 dp + 현재 집의 돈 중 최댓값을 가짐
    for i in range(2, n):
        if i == n-1:    # 첫번째 집을 턴 경우 제외
            dp[0][i] = dp[0][i-1]
            dp[1][i] = max(dp[1][i-1], dp[1][i-2] + money[i])
        else:
            dp[0][i] = max(dp[0][i-1], dp[0][i-2] + money[i])
            dp[1][i] = max(dp[1][i-1], dp[1][i-2] + money[i])

    return max(dp[0][-1], dp[1][-1])

m = [1,2,3]
print(solution(m))
    
