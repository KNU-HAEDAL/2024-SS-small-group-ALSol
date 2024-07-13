def solution(want, number, discount):
    result = 0
    #want(key)와 number(value)로 딕셔너리 만들기
    hash_table = dict()
    for i in range(len(want)):
        hash_table[want[i]] = number[i]
   
    for j in range(len(discount) % 10 +1):
        count = 0
        #discount에서 10개씩 슬라이싱
        slice_discount= discount[j:j+10]
       
        #해시테이블 수 만큼 돌면서 슬라이싱한 discount와 개수비교
        for k in range(len(hash_table)):
            if hash_table[want[k]] == slice_discount.count(want[k]):
                count += 1
        if count == len(hash_table):
            result += 1 
    return result


want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1] 
discount = ["chicken", "apple", "apple", "banana", "rice",
"apple", "pork", "banana", "pork", "rice", "pot",
"banana", "apple", "banana"]
print(solution(want, number, discount))