# 단품 메뉴를 조합하기 위해 조합 사용
# 조합된 세트 메뉴들의 갯수를 세기 위해 Counter 사용
from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    # 음식 x개로 구성할 수 있는 음식 조합 중 가장 큰 조합 찾아 추가하는 for문
    for c in course:
        menu = []   # 초기화

        # 구성할 수 있는 모든 조합 찾는 for문 
        for o in orders:
            o = sorted(o)   # 'AB', 'BA' 같은 조합도 같도록 하기 위해 정렬 후 조합 사용
            menu.extend((combinations(o, c)))
        
        # menu에서 나온 값들의 갯수를 dict 형태로 저장
        count = Counter(menu)

        # count에 음식이 존재하며 나온 횟수가 최소 2개 이상이면 추가 가능
        if len(count) != 0 and max(count.values()) >= 2:
            # value값이 최대인 key를 answer에 추가
            for key in count:
                if count[key] == max(count.values()):
                    key = "".join(key)
                    answer.append(key)
    
    answer.sort()        

    return answer

order = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]
print(solution(order, course))
