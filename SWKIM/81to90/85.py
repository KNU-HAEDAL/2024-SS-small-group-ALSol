def solution(N, stations, W):
    answer = 0
    aparts = []
    start = 0

    # 지기국 간의 전파가 닿지 않는 아파트의 갯수 구하기
    for s in stations:
        end = s - W

        if start < end:
            aparts.append(end - start - 1)
        
        start = s + W
    
    aparts.append(N - start)
    
    # 전파가 닿지 않는 아파트에 세울 지기국의 최솟값 구하기
    for i in aparts:
        if i % (W * 2 + 1) == 0:
            answer += i // (W*2 + 1)
        else:
            answer += i // (W*2 + 1) + 1
    
    return answer

print(solution(16, [9], 2))
