def solution(progresses, speeds):
    answer = []
    top = 0

    for i in range(len(progresses)):
        # 100%가 되기까지의 기간 계산
        if (100 - progresses[i]) % speeds[i] == 0:
            data = (100 - progresses[i])//speeds[i]
        else:
            data = (100 - progresses[i])//speeds[i] + 1
        
        # 해당 데이터가 앞의 데이터보다 큰지 비교하여 연산 
        if data > top:
            top = data
            answer.append(1)
        else:
            answer[-1] += 1
    
    return answer


    

