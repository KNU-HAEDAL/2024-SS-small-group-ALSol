def solution(n):
    dp = [1]*(n+1)
    for i in range(2, n+1):
        #  피보나치 수열처럼 아래 식을 만족한다
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
    
    return dp[n]