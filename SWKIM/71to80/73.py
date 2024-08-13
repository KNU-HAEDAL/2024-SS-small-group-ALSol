def solution(n):
    fibo = [0, 1]

    # fibo(n) = fibo(n-2) + fibo(n-1)을 활용
    # 재귀 사용시 메모리 초과
    for i in range(2, n+1):
        fibo.append(fibo[i-2] + fibo[i-1])
    
    return fibo[n] % 1234567

print(solution(5))