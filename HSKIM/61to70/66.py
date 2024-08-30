from collections import Counter

def solution(topping):
    answer = 0
    topping_cnt = Counter(topping)  # 각 토핑 종류별로 개수 세기
    person_1 = set()    # 형이 받을 토핑의 종류
    person_2 = len(topping_cnt)  # 동생이 받을 토핑의 종류 개수

    for i in topping:
        topping_cnt[i] -= 1  # 동생의 해당 토핑 수 감소
        person_1.add(i)  # 형에게 해당 토핑 추가

        # 동생에게 해당 토핑이 더 이상 없으면 토핑 종류 개수 감소
        if topping_cnt[i] == 0:
            person_2 -= 1
        
        # 형과 동생의 토핑 종류 수가 같으면 경우의 수 증가
        if len(person_1) == person_2:
            answer += 1
        elif len(person_1) > person_2:  # 형의 토핑 종류가 더 많아지면 종료
            break
    
    return answer

topping = [1, 2, 3, 1, 4]
print(solution(topping))  
