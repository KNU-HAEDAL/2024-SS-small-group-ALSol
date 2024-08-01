# 백트래킹을 활용한 dfs 함수
def dfs(info_1, info_2, target, start, cnt, distance):
    # 활을 모두 다 쐈을 경우
    if cnt == 0:
        score_1 = 0
        score_2 = 0

        # 어피치와 라이언의 점수 계산
        for i in range(11):
            if info_1[i] < info_2[i]:
                score_2 += 10 - i
            elif info_1[i] > info_2[i]: 
                score_1 += 10 - i
            elif info_1[i] == info_2[i] and info_1[i] != 0:
                score_1 += 10 - i

        # 라이언의 점수가 어피치보다 더 높을 경우
        # 두 선수의 점수 차를 계산하여 점수 차가 최대인 경우 반환    
        if score_2 > score_1:   
            temp = score_2 - score_1

            if temp > distance: # 점수 차가 기존보다 더 큰 경우
                target = info_2.copy()
                distance = temp
            elif temp == distance:  # 점수 차가 같은 경우
                # 가장 낮은 점수를 맞힌 갯수를 기준으로 반환
                for i in range(10, -1, -1):
                    if info_2[i] > target[i]:
                        target = info_2.copy()
                        break
                    elif info_2[i] < target[i]:
                        break
        
        # 점수 차가 최대인 경우의 과녁 정보와 점수 차 반환
        return target, distance
    # 활을 덜 쏜 경우
    else:
        for i in range(start, 11):
            # 0점 과녁을 조준하고 남은 활 수가 남은 경우
            # 남은 활을 모두 0점 과녁에 쏜다.
            if i == 10 and cnt > 0:
                info_2[i] = cnt
                target, distance = dfs(info_1, info_2, target, i+1, 0, distance)
                info_2[i] = 0
            # 남을 활 수가 어피치가 쏜 i점의 활 수보다 큰 경우
            elif cnt > info_1[i]:
                info_2[i] = info_1[i] + 1   # 어피치보다 한발 더 많이 맞춘다.
                target, distance = dfs(info_1, info_2, target, i+1, cnt - info_2[i], distance)
                info_2[i] = 0
    return target, distance


def solution(n, info):
    info_2 = [0 for _ in range(11)]
    target = [0 for _ in range(11)]

    target, distance = dfs(info, info_2, target, 0, n, -1)

    if distance == -1:  # 라이언이 이길 수 없다면 [-1] 반환
        return [distance]
    
    return target

info = [0,0,1,2,0,1,1,1,1,1,1]
print(solution(9, info))