def solution(s):
    answer = [0, 0]

    while s != '1':
        answer[0] += 1  # 이진 변환 횟수 증가
        zero_count = s.count('0')  # 0의 개수 세기
        answer[1] += zero_count  # 제거된 0의 개수 누적
        s = bin(len(s) - zero_count)[2:]  # 0을 제거한 문자열의 길이를 이진수로 변환

    return answer

s = "1111111"
print(solution(s))
