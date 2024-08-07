def solution(n):
    # n을 문자열로 바꾼 후 정수를 기준으로 내림차순 정렬
    answer = sorted(str(n), key=lambda x: int(x), reverse=True)
    return "".join(answer)

print(solution(118372))