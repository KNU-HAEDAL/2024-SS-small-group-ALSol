# 방정식을 세워 해결
def solution(blue, white):
    answer = []
    x = 1
    a = (blue + 4) // 2 # 가로와 세로길이의 합
    b = blue + white    # 가로와 세로길이의 곱
    
    while True:
        if x**2 - a*x + b == 0: # 해당 값을 만족하는 x값인 경우
            answer.append(x)
            break

        x += 1
    
    # 위 식을 만족하는 또 다른 값을 찾아 추가
    answer.append(a - answer[0])
    answer.sort(reverse=True)   # 가로길이가 더 길기에 내림차순으로 정렬
    return answer

print(solution(10, 2))
