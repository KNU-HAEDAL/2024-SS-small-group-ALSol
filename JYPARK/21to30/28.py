def solution(N, A, B):
    answer = 0
    while True:
        if A == B:
            break
        if A % 2 == 0:
            A = A // 2
        else:
            A = A // 2 +1
        if B % 2 == 0:
            B = B // 2
        else:
            B = B // 2 + 1
        answer += 1
    return answer

N = 8
A = 4
B = 7
print(solution(N, A, B))