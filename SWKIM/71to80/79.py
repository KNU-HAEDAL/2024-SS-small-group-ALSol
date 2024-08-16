def solution(strs, t):
    size = len(t)
    dp = [float("inf") for _ in range(size+1)]
    dp[0] = 0   # 일관되게 하기 위함

    # 단어 조각의 길이는 1~5이므로 현재 위치의 알파벳 + 이전 알파벳을 조합
    # 그리하여 만든 단어가 strs에 있는지 확인하고 만일 있다면 dp[단어가 시작된 idx - 1] + 1 을 현재 dp에 저장
    # 이 과정을 반복하여 최솟값을 dp에 저장하는 방식
    for i in range(1, size+1):
        for j in range(1, 6):
            if i - j == -1:
                break

            if t[i-j:i] in strs:
                dp[i] = min(dp[i], dp[i-j] + 1)
            

    if dp[-1] == float('inf'):
        return -1      
    return dp[-1]

strs = ['ba', 'an', 'nan', 'ban', 'n']
t = 'banana'
print(solution(strs, t))