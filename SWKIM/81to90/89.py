def solution(s):
    answer = []

    for num in s:
        cnt = 0 # 110이 나온 횟수
        string = '' # 110이 제거된 숫자

        # 숫자에서 110인 부분을 없애고 카운트 증가
        for ch in num:
            string += ch

            if len(string) > 2 and string[-3:] == '110':
                string = string[:-3]
                cnt += 1

        check = False   # 남은 숫자에 0이 있는지 검사

        # 가장 뒤에 있는 0의 뒤에 110 추가
        for i in range(len(string)-1, -1, -1):
            if string[i] == '0':
                check = True
                answer.append(string[:i+1] + '110'*cnt + string[i+1:])
                break
        # 남은 문자열에 0이 없는 경우
        if not check:
            answer.append('110'*cnt + string)
        
        
    return answer

print(solution(	["1101", "100110110", "0110110111"]))