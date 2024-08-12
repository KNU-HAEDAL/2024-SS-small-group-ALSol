def creat_hash(str):
    p = 31
    m = 1_000_000_007
    hash_value = 0
    for char in str:
        # ord() : 단일 문자를 입력받아 그 문자의 유니코드(Unicode) 또는 아스키 값을 반환
        hash_value = (hash_value * p + ord(char)) % m 
    return hash_value

def solution(string_list, query_list):
    hash = [creat_hash(str) for str in string_list]

    result = []
    for query in query_list:
        query_hash = hash(query)
        if query_hash in hash:
            result.append(True)
        else:
            result.append(False)

    return result

