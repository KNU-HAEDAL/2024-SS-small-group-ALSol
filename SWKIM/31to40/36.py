def solution(phone_book):
    # 정렬하여 시작 숫자가 최대한 같도록 함
    phone_book.sort()

    for i in range(len(phone_book)-1):
        length_1 = len(phone_book[i])
        length_2 = len(phone_book[i+1])

        # 앞의 단어 길이가 뒤의 단어 길이보다 짧다면
        if length_1 < length_2:
            # 앞의 단어를 접두어로 가진다면
            if phone_book[i] == phone_book[i+1][:length_1]:
                return False
        
    return True

phone_book = ["119", "97674223", "1195524421"]
print(solution(phone_book))
