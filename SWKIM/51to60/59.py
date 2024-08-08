def solution(numbers):
    # 숫자를 문자열로 바꿔 3을 곱한 뒤 4번째 자릿수까지의 수를 비교해 정렬
    numbers = sorted(numbers, key=lambda x: str(str(x)*3)[:4], reverse=True)

    # 결과가 0000...000 인 경우 0 반환
    if int("".join(str(x) for x in numbers)) == 0:
        return '0'
    
    return "".join(str(x) for x in numbers)

numbers = [8, 87, 889]
print(solution(numbers))

