from functools import cmp_to_key

def compare(a, b):
    if a + b > b + a:
        return -1
    elif a + b < b + a:
        return 1
    else:
        return 0

def solution(numbers):
    # numbers를 문자열로 변환
    numbers = list(map(str, numbers))
    
    # 커스텀 비교 함수를 사용하여 정렬
    numbers.sort(key=cmp_to_key(compare))
    
    # 결과가 000...000 인 경우 0 반환
    if numbers[0] == '0':
        return '0'
    
    # 정렬된 숫자들을 이어붙여 반환
    return ''.join(numbers)

numbers = [6, 10, 2]
print(solution(numbers))
