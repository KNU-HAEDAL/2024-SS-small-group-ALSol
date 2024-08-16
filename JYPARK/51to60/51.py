def distribution(arrows, score, arrow_per_person=None, idx=0):
    if arrow_per_person is None:
        arrow_per_person = [0] * score

    if arrows == 0:
        return [tuple(arrow_per_person)]

    distributions = []

    for i in range(idx, score):
        if arrows > 0:
            arrow_per_person[i] += 1
            next_distributions = distribution(arrows - 1, score, arrow_per_person, i)
            distributions.extend(next_distributions)
            arrow_per_person[i] -= 1

    return distributions    

def solution(n, info):
    answer = []
    maxv = 0
    real = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    all_distributions = distribution(n, 11)
    
    for temp in all_distributions:
        ryan = 0
        muzi = 0
        for i in range(len(temp)):
            if temp[i] or info[i]:
                if temp[i] > info[i]:
                    ryan += real[i]
                else:
                    muzi += real[i]
        
        gap = ryan - muzi
        
        if gap > maxv:
            answer = []
            answer.append(temp)
            maxv = gap
        elif gap < maxv:
            continue
        else:
            answer.append(temp)
    
    if not answer:
        return [-1]
    elif maxv == 0:
        return [-1]
    
    idx = -1
    for i in range(len(answer[0])-1, -1, -1):
        maxv = -float('inf')
        for a in answer:
            if a[i] == 0:
                continue
            if maxv < a[i]:
                maxv = a[i]
        if maxv > 0:
            idx = i
            break
    
    answer.sort(key = lambda x:-x[idx]) 

    return answer[0]

n, info = 5, [2,1,1,1,0,0,0,0,0,0,0]
n, info = 1, [1,0,0,0,0,0,0,0,0,0,0]	
n, info = 9, [0,0,1,2,0,1,1,1,1,1,1]
n, info = 10, [0,0,0,0,0,0,0,0,3,4,3]
print(solution(n, info))