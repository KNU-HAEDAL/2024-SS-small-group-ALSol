def solution(string_list, query_list):
    key_list = set(string_list)
    answer = []

    # string_list와 query_list의 값이 중복되지 않도록 set 사용
    for i in query_list:
        key_list.add(i)
    
    hashtable = dict()
    
    # key_list에 저장된 값에서 string_list에 포함됐다면 1, 아니면 0
    for i in key_list:
        hashtable[i] = 0
    
    for i in string_list:
        hashtable[i] = 1
    
    # query_list의 값이 string_list에 포함됐다면 True, 아니면 False
    for i in query_list:
        if hashtable[i] == 1:
            answer.append(True)
        else:
            answer.append(False)
    
    return answer

print(solution(["a", "b", "c"], ["b", "d", "e", "a"]))

 