from itertools import combinations # 메뉴에서 n 가지를 뽑아 메뉴 조합 구성
from collections import Counter # 메뉴 조합의 빈도를 세기 위함

def solution(orders, course):
    answer = []
    
    for c in course:
        menu = []
        for order in orders:
            comb = combinations(
                sorted(order), c
            )
            menu += comb
        
        counter = Counter(menu)
        if (
            len(counter) != 0 and max(counter.values()) != 1
        ):
            for m, cnt in counter.items():
                if cnt == max(counter.values()):
                    answer.append("".join(m))
    
    return sorted(answer)

# orders = ['ABCFG', 'AC', 'CDE', 'ACDE', 'BCFG', 'ACDEH']
# print(solution(orders, [2, 3, 4]))
