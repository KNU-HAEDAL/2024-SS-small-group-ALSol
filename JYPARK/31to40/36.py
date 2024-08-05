#sort()는 리스트 자체를 정렬해준다. sorted는 정렬된 새로운 리스트를 반환해준다.
def solution(phone_book):
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):           #startswith() -> 접두사 여부 확인 함수
            return False
    return True

#phone_book = ["119", "97674223", "1195524421"]
#phone_book = ["123","456","789"]
phone_book = ["12","123","1235","567","88"]
solution(phone_book)