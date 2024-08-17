def solution(d, budget):
    answer = 0
    # 최대한 지원하기 위해 오름차순으로 정렬
    d.sort()

    for money in d:
        # 예산이 해당 부서의 신청금액보다 크거나 같은 경우
        if budget >= money:
            answer += 1
            budget -= money
        else:
            break
    
    return answer