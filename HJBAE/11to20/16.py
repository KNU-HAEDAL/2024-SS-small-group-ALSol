"""
각 기능은 진도가 100%일 때 서비스에 반영 가능
개발 속도 모두 달라서 뒤의 기능이 앞의 기능보다 먼저 개발될 수도 있음
but, 배포는 뒤의 기능이 앞의 기능 배포될 때 함께 배포되어야 함
배포 순서대로 작업 진도가 적힌 정수 배열 progresses
각 작업의 개발 속도가 적힌 정수 배열 speeds
"""

import math

def solution(progresses, speeds):
    answer = []
    cost_day = []

    # 작업 완료까지 남은 날짜 수 구하는거 걍 각자 나눠서 버리면 되잖아 -> ceil() 나오네

    for i in range(len(progresses)):
        cost_day.append(math.ceil((100 - progresses[i]) / speeds[i]))

    # [7, 3, 9] 라는 결과가 나오는데 이걸 [2, 1]이 나오게...
    # 시작하는 일자 = 첫 번째 인덱스 소요 일수
    start_day = cost_day[0]
    count = 1

    for i in range(1, len(cost_day)):
        if cost_day[i] <= start_day:
            count += 1
        else:   # 더 큰 값이 나오면 일단 멈추고 저장하고 다시 시작한다는거잖아
            answer.append(count)
            count = 1
            start_day = cost_day[i]
    
    answer.append(count)
    return answer


progresses = [93, 30, 55]
speeds = [1, 30, 5]

print(solution(progresses, speeds))

progresses_2 = [95, 90, 99, 99, 80, 99]
speeds_2 = [1, 1, 1, 1, 1, 1]
print(solution(progresses_2, speeds_2))

# progresses speeds return
# [93, 30, 55] [1, 30, 5] [2, 1]

# [95, 90, 99, 99, 80, 99] [1, 1, 1, 1, 1, 1] [1, 3, 2]
# [5, 10, 1, 1, 20, 1]