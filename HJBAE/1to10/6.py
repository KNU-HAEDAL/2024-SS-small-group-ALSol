N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

def solution(N, stages):
    fail_stage = [[0, 0] for _ in range(N)]  # [스테이지 도달, 스테이지 실패]

    for stage in stages:
        if stage <= N:  # 마지막 스테이지 클리어하지 못한 플레이어만 카운팅
            fail_stage[stage - 1][1] += 1
        for i in range(min(stage, N)):  # 스테이지 도달한 플레이어 수 카운팅
            fail_stage[i][0] += 1

    fail_rate = []
    for i in range(N):
        if fail_stage[i][0] == 0:
            fail_rate.append((i + 1, 0))
        else:
            fail_rate.append((i + 1, fail_stage[i][1] / fail_stage[i][0]))

    fail_rate.sort(key=lambda x: (-x[1], x[0]))

    sorted_stages = [stage for stage, rate in fail_rate]
    return sorted_stages

print(solution(N, stages))

# 실패율 = 스테이지에 도달했으나 아직 클리어하지 못한 플레이어 수 / 스테이지에 도달한 플레이어 수