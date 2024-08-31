def solution(lottos, win_nums):
    win_nums = set(win_nums)
    # 등수를 계산하는 dict
    score = {x: 7 - x for x in range(1, 7)}
    score[0] = 6
    
    cnt = 0 # 맞는 숫자의 수
    zero = 0    # 0의 수

    # 맞는 수와 0의 갯수 계산
    for num in lottos:
        if num == 0:
            zero += 1
        else:
            if num in win_nums:
                cnt += 1
    
    # 최고 등수와 최소등수 계산
    answer = [score[cnt + zero], score[cnt]]

    return answer

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))