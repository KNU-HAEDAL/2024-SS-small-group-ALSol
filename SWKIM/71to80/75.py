def solution(triangle):
    dp = [[0 for _ in range(i+1) ] for i in range(len(triangle))]
    dp[0][0] = triangle[0][0]

    # 현재 칸에서 만들 수 있는 최댓값을 찾아 저장
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            elif j == len(triangle[i]) - 1:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
    
    return max(dp[-1])  # 맨 아래층에서의 최댓값 반환

triangle = [[7], [3, 8], [8,1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))