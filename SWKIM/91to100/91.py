def solution(numbers):
    answer = 0

    # set으로 변환해 더 빠르게 찾기 위함
    numbers = set(numbers)

    # 찾을 수 없는 경우 더하기
    for i in range(10):
        if i not in numbers:
            answer += i
    
    return answer

print(solution([1,2,3,4,6,7,8,0]))