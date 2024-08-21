"""
전화번호부에 적힌 전화번호 중 한 번호가 다른 번호의 접두어인 경우가 있는지 확인
전화번호가 다음과 같을 경우 구조대 전화번호는 영석이 전화번호 접두사
구조대 : 119
박준영 : 97 674 223
지영석 : 11 9552 4421
전화번호부에 적힌 전화번호를 담은 배열 phone_book이 solution() 함수의 매개변수로 주어질 때
어떤 번호가 다른 번호의 접두어이면 False, 그렇지 않으면 True를 반환하는 solution() 함수 작성
"""

def solution(phone_book):
    phone_book.sort()

    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False
    return True 

phone_book1 = ["119", "97674223", "1195524421"]
# return1 = False
print(solution(phone_book1))
phone_book2 = ["123", "456", "789"]
# return2 = True
print(solution(phone_book2))
phone_book3 = ["12", "123", "1235", "567", "88"]
# return3 = False
print(solution(phone_book3))