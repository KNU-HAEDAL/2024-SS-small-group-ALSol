"""
order은 손님들이 주문하던 단품메뉴들
최소 2명 이상의 손님으로부터 주문된 단품 메뉴 조합에 대해서만 코스요리 메뉴 후보에 포함
course는 추가하고 싶은 단품 메뉴
"""
from itertools import combinations
from collections import Counter

def solution(orders, course):
    result = []

    for c in course:
        comb_list = []

        for order in orders:
            # 각 주문 알파벳 순으로 정렬 + combinations를 사용해서 주문된 단품 메뉴 조합 생성
            comb_list += combinations(sorted(order), c)

        # 생성된 조합들 Counter 사용해서 셈 -> 각 조합 몇 번 주문되었는지 check
        most_common_comb = Counter(comb_list).most_common()

        # 2명 이상 주문한 조합 중 가장 많이 주문한 조합 result에 추가
        result += [comb for comb, count in most_common_comb if count > 1 and count == most_common_comb[0][1]]

    return [''.join(comb) for comb in sorted(result)]

orders1 = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course1 = [2, 3, 4]
# result1 = ["AC", "ACDE", "BCFG", "CDE"]

orders2 = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course2 = [2, 3, 5]
# result2 = ["ACD", "AD", "ADE", "CD", "XYZ"]

orders3 = ["XYZ", "XWY", "WXA"]
course3 = [2, 3, 4]
# result3 = ["WX", "XY"]

print(solution(orders1, course1))
print(solution(orders2, course2))
print(solution(orders3, course3))