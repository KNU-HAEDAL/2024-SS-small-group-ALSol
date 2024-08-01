def solution(progresses, speeds):
    from math import ceil

    # 각 작업이 완료되는 일수를 계산
    days = [ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
    
    result = []
    while days:
        # 첫 번째 작업의 완료 일자를 기준으로 배포
        deploy_day = days.pop(0)
        count = 1
        
        # 같은 날 배포 가능한 작업들을 체크
        while days and days[0] <= deploy_day:
            days.pop(0)
            count += 1
        
        result.append(count)
    
    return result

print(solution([93, 30, 55], [1, 30, 5])) 
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])) 
