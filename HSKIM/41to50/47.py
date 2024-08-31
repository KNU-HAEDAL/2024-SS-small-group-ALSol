def solution(N):
    answer = []

    def backtrack(sum, arr, start):
        if sum == 10:
            answer.append(arr)
            return
        
        for i in range(start, N+1): # 합이 10보다 작거나 같으면 재귀적으로 실행
            if sum + i <= 10:
                backtrack(sum + i, arr + [i], i + 1)
    
    backtrack(0, [], 1)
    
    return answer

print(solution(5))