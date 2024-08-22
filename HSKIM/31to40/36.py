def solution(phone_book):
    # 사전 순으로 앞서는 것을 앞으로 정렬
    phone_book.sort( )

    for i in range(len(phone_book) - 1):
        # startswith 는 현재 문자열이 사용자가 지정하는 특정 문자로 시작하는지 확인하는 함수
        if phone_book[i + 1].startswith(phone_book[i]):
            return False
    return True

phone_book = ["119", "97674223", "1195524421"]
print(solution(phone_book))