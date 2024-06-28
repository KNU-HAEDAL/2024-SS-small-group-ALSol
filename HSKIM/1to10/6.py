def solution(N, stages):
    fail = { }

    # 실패율 계산
    for i in range(1, N + 1):
        player = 0
        not_sucess = 0
        for stage in stages:
            if i == stage:
                not_sucess += 1
            if i <= stage:
                player += 1

        if player == 0:
            fail[i] = 0
        else:
            fail[i] = not_sucess / player
    
    # 실패율 내림차순으로 정리
    result = sorted(fail, key=lambda x : fail[x], reverse=True)

    return result

s = [2, 1, 2, 6, 2, 4, 3, 3]

print(solution(5, s))
