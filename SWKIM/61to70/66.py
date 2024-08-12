from collections import Counter
# 토핑 종류들을  counter를 사용해 해결
def solution(topping):
    answer = 0
    topping_cnt = Counter(topping)
    person_1 = set()    # 형이 받을 토핑의 종류
    person_2 = len(topping_cnt) # 동생이 받을 토핑의 종류

    for i in topping:
        # 동생에게서 가져온 토핑 조각을 형에게 전달
        topping_cnt[i] -= 1
        person_1.add(i)

        # 동생에게 해당 토핑이 더이상 없는 경우
        if topping_cnt[i] == 0:
            person_2 -= 1
        
        # 토핑 종류의 갯수가 서로 같은 경우
        if len(person_1) == person_2:
            answer += 1
        elif len(person_1) > person_2:  # 형이 동생보다 토핑 종류가 더 많으면 종료
            break
    
    return answer


topping = [1, 2, 3,1,4]
print(solution(topping))