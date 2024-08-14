def solution(land):
    dp = [[0]*4 for _ in range(len(land)+1)]

    for i in range(1, len(land) + 1):
        for j in range(4):
            # 현재 위치의 값 + 이전 행의 같은 열이 아닌 숫자 중 최댓값
            dp[i][j] = max(dp[i-1][:j] + dp[i-1][j+1:]) + land[i-1][j]
    
    return max(dp[-1])

land = [[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]
print(solution(land))