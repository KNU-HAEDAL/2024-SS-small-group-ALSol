from collections import Counter
# 리스트에 저장된 값 각각의 갯수를 dict으로 변환하기 위함

def solution(want, number, discount):
    shopping_basket = {}
    answer = 0
    length = 0

    # want와 number를 key와 value로 하는 dict 생성
    for i in range(len(want)):
        shopping_basket[want[i]] = number[i]
        length += number[i]
    
    # 10일동안 할인하는 상품목록이 원하는 상품목록과 같은지 계산
    for i in range(len(discount) - length + 1):
        check = True 
        
        # 10일 동안 할인하는 상품의 갯수 계산
        item = Counter(discount[i:i+length])

        # 원하는 상품의 갯수와 할인하는 상품의 갯수가 같은지 비교
        for j in want:
            if shopping_basket[j] != item[j]:
                check = False
                break
        
        if check:
            answer += 1
    
    return answer