def solution(N, stages):
    answer = []
    cnt=0
    total=len(stages)
    rates=[]
    for i in range(1,N+2):
        cnt=stages.count(i)
        if total==0:
            failure_rate=0
        else:
            failure_rate=cnt/total
        if i<N+1:
            rates.append((failure_rate,i))
        total-=cnt
    rates.sort(key = lambda x :x[0],reverse=True)
    answer=[k for stage,k in rates]
    return answer