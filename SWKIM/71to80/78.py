def solution(board):
    answer = 0
    n = len(board)
    m = len(board[0])
    dp = [[0 for _ in range(m+1)]for _ in range(n+1)]
    
    # board가 [1][1]에서 시작하도록 함
    for i in range(n):
        for j in range(m):
            dp[i+1][j+1] = board[i][j]


    for i in range(1, n+1):
        for j in range(1, m+1):
            # 해당 dp가 1인 경우 현재 위치를 우측 아래 꼭짓점으로 하는 정사각형의 변 계산
            if dp[i][j] == 1:
                # 만들 수 있는 정사각형 변의 길이가 1보다 큰 경우
                if (dp[i-1][j-1] > 0 and 
                    dp[i][j-1] > 0 and 
                    dp[i-1][j] > 0):
                    
                    x = min(dp[i][j-1], dp[i-1][j])

                    if x > dp[i-1][j-1]:     # dp[i-1][j-1]이 dp[i-1][j]와 dp[i][j-1]의 최솟값보다 작은 경우
                        dp[i][j] = x
                    else:
                        dp[i][j] = x + 1
                    
                answer = max(answer, dp[i][j])
                
    # 정사각형의 넓비 계산
    return answer * answer

b = 	[[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]
print(solution(b))