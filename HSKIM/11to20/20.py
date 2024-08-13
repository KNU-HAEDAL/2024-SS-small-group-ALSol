def solution(participant, completion):
    h = {}

    for p in participant:
        if p in h:
            h[p] += 1
        else:
            h[p] = 1
        
        for c in completion:
            h[p] -= 1
        
        # .keys()는 딕셔너리의 모든 키(key)를 반환
        for key in h.keys():
            if h[key] > 0:
                return key