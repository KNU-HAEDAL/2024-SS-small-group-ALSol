def solution(want, number, discount):   # 쇼핑리스트 출력

    shop_list = {}
    for i in range(len(want)):
        shop_list[want[i]] = number[i]
    
    count = 0
    for i in range(len(discount) - 9):
        discount_list = {}  #할인 받을 수 있는 상품 리스트

        for j in range(i, i + 10):    # range(j + 10) -> range(i, i + 10)
            item = discount[j]
            if item in discount_list:   
                discount_list[item] += 1    #할인 받을 수 있는 상품 갯수를 차곡차곡 쌓아나간다는 느낌으로..
            else:
                discount_list[item] = 1
        
        if (shop_list == discount_list):
            count += 1
    return count
        
want1 = ["banana", "apple", "rice", "pork", "pot"]    #원하는 제품 문자열
number1 = [3, 2, 2, 2, 1]   #원하는 제품의 수량
# 마트에서 할인하는 제품
discount1 = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]

want2 = ["apple"]
number2 = [10]
discount2 = ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]

print(solution(want1, number1, discount1))
print(solution(want2, number2, discount2))

"""
바나나 3 사과 2 쌀 2 돼지고기 2 냄비 1
치킨 사과 사과 바나나 쌀 사과 돼지고기 바나나 돼지고기 쌀 냄비 바나나 사과 바나나
    사과 사과 바나나 쌀     돼지고기 바나나 돼지고기 쌀 냄비 바나나
"""