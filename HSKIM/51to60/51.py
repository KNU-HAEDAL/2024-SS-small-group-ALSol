def dfs(info_1, info_2, cnt, start, best_target, max_diff):
    if cnt == 0:  # 모든 화살을 다 쏜 경우
        score_1, score_2 = 0, 0
        
        for i in range(11):
            if info_2[i] > info_1[i]:  # 라이언이 더 많이 맞춘 경우
                score_2 += 10 - i
            elif info_1[i] > 0:  # 어피치가 맞춘 경우
                score_1 += 10 - i
        
        diff = score_2 - score_1
        if diff > max_diff: # 점수 차가 기존보다 더 큰 경우
            return info_2.copy(), diff
        elif diff == max_diff:  # 점수 차가 같은 경우
            for i in range(10, -1, -1):
                if info_2[i] > best_target[i]:
                    return info_2.copy(), diff
                elif info_2[i] < best_target[i]:
                    break
        return best_target, max_diff
    
    for i in range(start, 11):
        if i == 10:  # 남은 화살을 모두 0점에 쏜다.
            info_2[i] = cnt
            return dfs(info_1, info_2, 0, i + 1, best_target, max_diff)
        if cnt > info_1[i]:  # 라이언이 어피치보다 많이 맞출 수 있는 경우
            info_2[i] = info_1[i] + 1
            best_target, max_diff = dfs(info_1, info_2, cnt - info_2[i], i + 1, best_target, max_diff)
            info_2[i] = 0
    
    return best_target, max_diff

def solution(n, info):
    best_target, max_diff = dfs(info, [0] * 11, n, 0, [0] * 11, -1)
    return best_target if max_diff > 0 else [-1]

info = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print(solution(1, info))
