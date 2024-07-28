def solution(N):
    answer = []

    # 백트래킹 함수
    def backtrack(sum, arr, start):
        # 합이 10이 되면 answer에 추가
        if sum == 10:
            answer.append(arr)
            return
        
        # 합이 10보다 작거나 같으면 재귀적으로 실행
        for i in range(start, N+1):
            if sum + i <= 10:
                backtrack(sum + i, arr + [i], i+1)
    
    backtrack(0, [], 1)
    
    return answer

print(solution(5))