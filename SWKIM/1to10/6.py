def solution(n, stages):
    rate = {}
    total = len(stages)

    for stage in range(1, n+1):
        if total != 0:
            cnt = stages.count(stage)
            rate[stage] = cnt / total
            total -= cnt
        else:
            rate[stage] = 0

    result = sorted(rate, key=lambda x : rate[x], reverse=True)     
    
    return result

print(solution(5, [2,1,2,6,2,4,3,3]))
print(solution(4, [4,4,4,4,4]))
