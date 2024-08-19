def solution(cap, n, deliveries, pickups):
    answer = 0
    deliveries = [0] + deliveries
    pickups = [0] + pickups

    d = 0
    p = 0

    # 가장 멀리 있는 곳부터 방문하면서 진행
    for i in range(n, 0, -1):
        d += deliveries[i]
        p += pickups[i]

        # 현재 지닌 배달 및 수거 박스가 양수인 경우
        # 음수라면 최대인 방문지가 아님
        while d > 0 or p > 0:
            d -= cap
            p -= cap

            answer += i*2

    
    return answer
            

print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))