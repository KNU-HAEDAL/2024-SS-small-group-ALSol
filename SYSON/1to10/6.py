def solution(N, stages):
    stage_count = [0]*(N+2)
    failure_rate = []

    for statge in stages:
        stage_count[stage]+=1

        total_player = len(stages)


    for i in range(1, N+1):
        if total_player>0:
            failure_rate.append((i, stage_count[i] / total_player))
            total_player -=stage_count[i]
        else:
            failure_rate.append((i, 0))


        failure_rate.sort(key = lambda x: (-x[1], x[0]))

        return[stage[0] for stage in failure_rate]

        N = 5
        stages = [2, 1, 2, 6, 2, 4, 3, 3]
        print(solution(N, stages))
