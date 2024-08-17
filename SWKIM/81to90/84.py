from collections import Counter
def solution(k, tangerine):
    answer = 0
    tangerine = Counter(tangerine)  # 갯수 세기

    tangerine_key = tangerine.keys()
    # 갯수에 따라 내림차순으로 정렬
    tangerine_key = sorted(tangerine_key, key= lambda x: tangerine[x], reverse=True)

    for key in tangerine_key:
        if tangerine[key] < k:  # 귤을 모드 넣을 수 있는 경우
            k -= tangerine[key]
            answer += 1
        else:   # 일부만 넣을 수 있는 경우
            answer += 1
            break
    
    return answer