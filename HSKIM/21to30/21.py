def solution(want, number, discount):
    want_dic = {}
    for i in range(len(want)):
        want_dic[want[i]] = number[i]
    
    day = 0
    for i in range(len(discount) - 9):
        discount_dic = {}

        for j in range(i, i + 10):
            if discount[j] in want_dic:
                # value = dictionary.get(key, default_value)
                # default_value (선택적): 키가 딕셔너리에 없을 때 반환할 값
                discount_dic[discount[j]] = discount_dic.get(discount[j], 0) + 1

        if discount_dic == want_dic:
            day += 1

    return day