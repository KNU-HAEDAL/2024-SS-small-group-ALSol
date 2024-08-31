from collections import deque

def solution(progresses, speeds):
    released_f = []
    day = 0
    count = 0

    while progresses:
        if progresses[0] + day * speeds[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1

            if not progresses or progresses[0] + day * speeds[0] < 100:
                released_f.append(count)
                count = 0
        
        else:
            time +=1

    return released_f



progresses = [93, 30, 55]
speeds = [1, 30, 5]
print(solution(progresses, speeds))