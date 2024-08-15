"""
문자열 리스트 string_list와 쿼리 리스트 query_list가 있을 때
각 쿼리 리스트에 있는 문자열이 string_list의 문자열 리스트에 있는지 여부를 확인해야 함
문자열 있으면 True, 없으면 False
문자열의 존자 여부를 리스트 형태로 반환하는 solution() 함수를 작성

입력 문자열 영어 소문자로만
문자열 최대 길이 10^6
해시 충돌 X
p = 31, m = 1,000,000,007
"""

def find_hash(s, p = 31, m = 1_000_000_007):
    hash_value = 0
    pp = 1
    for c in s:
        hash_value = (hash_value + (ord(c) - ord('a') + 1) * pp) % m
        pp = (pp * p) % m
    return hash_value

def solution(string_list, query_list):
    hash_set = set(find_hash(s) for s in string_list)

    result = []
    for query in query_list:
        query_hash = find_hash(query)
        result.append(query_hash in hash_set)

    return result


string_list = ["apple", "banana", "cherry"]
query_list = ["banana", "kiwi", "melon", "apple"]
# return = [True, False, False, True]

print(solution(string_list, query_list))