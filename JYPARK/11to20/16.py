import math
def solution(progresses, speeds):
    answer = []
    left_days = [0] * len(progresses)

    for i in range(len(progresses)):
        left_days[i] = math.ceil((100 - progresses[i]) / speeds[i])
    
    count = 0
    max_day = left_days[0]
    for i in range(len(left_days)):
        if left_days[i] <= max_day:
            count += 1
        else:
            answer.append(count)
            count = 1
            max_day = left_days[i]
    answer.append(count)
    return answer

progresses = [93, 30, 55] 
speeds = [1, 30, 5] 
#progresses = [95, 90, 99, 99, 80, 99] 
#speeds = [1,1,1,1,1,1]
print(solution(progresses, speeds))
