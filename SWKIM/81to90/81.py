def solution(items, weight_limit):
    answer = 0

    # 1kg 당 가치를 계산해 추가
    for item in items:
        item.append(item[1]/item[0])
    
    # 1kg 당 가치가 가장 높은 순으로 정혛
    items = sorted(items, key= lambda x: x[2], reverse=True)
    
    for item in items:
        # 해당 물건을 모두 넣을 수 있는 경우
        if weight_limit - answer > item[0]:
            answer += item[1]
            weight_limit -= item[0]
        # 해당 물건을 일부만 넣어야 하는 경우
        else:
            answer += item[2]*weight_limit
            break

    
    return round(answer, 2)

items = [[10, 60], [20,100], [30,120]]
print(solution(items, 50))   

