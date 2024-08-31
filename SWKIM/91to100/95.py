def solution(alp, cop, problems):
    # problems에서 가장 높은 코딩력과 알고력 저장
    max_alp = max(p[0] for p in problems)
    max_cop = max(p[1] for p in problems)

    # 현재 알고력과 코딩력과 문제의 가장 높은 코딩력, 알고력 중 큰 값을 저장
    # 현재 알고력과 코딩력이 문제에 주어진 가장 높은 알고력과 코딩력보다 높은 경우가 있기 때문
    max_alp = max(alp, max_alp)
    max_cop = max(cop, max_cop)

    # dp를 통해 동적으로 해결하기 위함
    dp = [[float("inf") for _ in range(max_cop+1)] for _ in range(max_alp+1)]
    dp[alp][cop] = 0

    for i in range(alp, max_alp+1):
        for j in range(cop, max_cop+1):
            # problems을 활용하지 않고 코딩력과 알고력을 얻는 경우
            if j < max_cop:
                dp[i][j+1] = min(dp[i][j] + 1, dp[i][j+1])

            if i <max_alp:
                dp[i+1][j] = min(dp[i][j] + 1, dp[i+1][j])

            # problems을 활용해 코딩력과 알고력을 얻는 경우
            for p in problems:
                alp_req, cop_req, alp_rwd, cop_rwd, cost = p
                
                # 해당 문제를 풀 수 있는 경우
                if i >= alp_req and j >= cop_req:
                    # 현재 알고력과 코딩력에 문제를 풀어 얻는 알고력과 코딩력을 더해 저장
                    # 이때 문제를 다 풀 수 있을 만큼의 양만 있으면 되기에 아래처럼 min을 활용
                    x = min(i + alp_rwd, max_alp)
                    y = min(j + cop_rwd, max_cop)

                    dp[x][y] = min(dp[i][j] + cost, dp[x][y])

    # 모든 문제를 풀 수 있을 때의 드는 시간의 최솟값 반환
    return dp[-1][-1]

print(solution(0, 0, [[0, 3, 1, 0, 0], [5, 0, 0, 8, 1], [0, 10, 0, 0, 0]]))