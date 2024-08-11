# 이진 변환
def convert_binary(s):
    converted_s = ""
    zero = 0    # 0을 제거한 횟수
    
    # 0 제거
    for i in s:
        if i == '1':
            converted_s += '1'
        else:
            zero += 1
    # 문자열의 길이를 이진수로 변환
    converted_s = bin(len(converted_s))[2:]

    return converted_s, zero

def solution(s):
    answer = [0, 0]

    while True:
        s, zero = convert_binary(s)
        
        # 이진 변환한 횟수와 0을 제거한 횟수 추가
        answer[0] += 1 
        answer[1] += zero

        if s == '1':
            break

    return answer

s = "1111111"
print(solution(s))