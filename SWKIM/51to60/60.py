def solution(s):
    s = s[1:-1]
    arr = []
    answer = []
    # 문자열로 표현된 튜플을 리스트로 변환
    for i in range(len(s)):
        if s[i] == '{':
            stack = []
            num = ""
            while True:
                i += 1

                if s[i] == '}':
                    stack.append(int(num))
                    arr.append(stack)
                    break
                elif s[i] == ',':
                    stack.append(int(num))
                    num = ""
                else:
                    num += s[i]
        else:
            continue
    
    # 길이를 기준으로 오름차순 정렬
    arr = sorted(arr, key=lambda x: len(x))
    # 중복된 숫자가 아니면 answer에 추가
    for num in arr:
        for i in range(len(num)):
            if num[i] not in answer:
                answer.append(num[i])
                break
    
    return answer

s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
print(solution(s))