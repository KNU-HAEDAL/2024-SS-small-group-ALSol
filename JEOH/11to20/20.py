def solution(participant, completion):
    answer = ''
    d={}
    for i in participant:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for k in completion:
        d[k]-=1
    for answer in d.keys():
        if d[answer]>0:
            return answer