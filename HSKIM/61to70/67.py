def solution(blue, white):
    # 가로와 세로 길이의 합과 곱을 계산
    perimeter = (blue + 4) // 2
    area = blue + white
    
    for x in range(1, perimeter):
        if x * (perimeter - x) == area:  # 방정식을 만족하는 x를 찾음
            return [max(x, perimeter - x), min(x, perimeter - x)]  # 가로가 더 길게 정렬하여 반환

print(solution(10, 2))  
