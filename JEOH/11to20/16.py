import math
def solution(progresses,speeds):
    answer=[]
    n=len(progresses)
    days_left=[math.ceil((100-progresses[i]/speeds[i])for i in range(n))]
    c=0
    max_d=days_left[0]
    for i in range(n):
        if days_left[i]<=max_d:
            c+=1
        else:
            answer.append(c)
            c=1
            max_d=days_left[i]
    answer.append(c)
    return answer