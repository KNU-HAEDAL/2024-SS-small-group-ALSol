def solution(N):
    answer = 0

    # 2로 나누었을 때 1이 나오는 갯수 구하기
    while True:
        if N == 0:
            break

        if N % 2 == 1:
            answer += 1
        
        N = N // 2
    
    return answer

print(solution(5000))