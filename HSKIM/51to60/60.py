def solution(s):
    # 문자열에서 양쪽의 "{{"와 "}}"를 제거하고, 중괄호를 기준으로 split
    s = s[2:-2].split("},{")
    
    # 각 요소를 리스트로 변환
    arr = [list(map(int, x.split(','))) for x in s]
    
    # 길이 기준으로 오름차순 정렬
    arr.sort(key=len)
    
    answer = []
    for subset in arr:
        for num in subset:
            if num not in answer:
                answer.append(num)
                break
    
    return answer

s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
print(solution(s)) 
