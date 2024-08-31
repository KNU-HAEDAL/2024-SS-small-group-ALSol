def solution(gems):
    answer = [1, float("inf")]  
    start = 0
    
    # 보석의 종류과 갯수 확인
    gem_set = set(gems)
    gem_dict = {}
    size = len(gem_set)

    # 모든 보석이 담긴 가장 작은 구간을 탐색
    for end in range(len(gems)):
        # 보석이 dict에 없다면 삽입 혹은 +1
        if gems[end] in gem_dict:
            gem_dict[gems[end]] += 1
        else:
            gem_dict[gems[end]] = 1

        # 구간 처음과 마지막 보석이 같은 경우
        # -1 더하기
        if start != end and gems[start] == gems[end]:
            gem_dict[gems[start]] -= 1
            start += 1

            # 시작 보석이 구간 안의 해당 보석이 1보다 큰 경우
            # -1 더하기
            while start != end and gem_dict[gems[start]] > 1:
                gem_dict[gems[start]] -= 1
                start += 1

        # 해당 구간이 모든 보석이 담긴 경우
        # 길이를 비교해 더 짧은 경우를 저장
        if len(gem_dict) == size:
            if end - start < answer[1] - answer[0]:
                answer = [start + 1, end + 1]

        end += 1      

    return answer
