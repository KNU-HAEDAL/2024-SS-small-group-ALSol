# 도대체 해시가 뭐지..?
'''
키와 값을 매핑한다 > 딕셔너리랑 비슷하다? > 하지만 메모리 상으로 조금 더 효율적이다?
 > 충돌처리는 해줘야 한다 > 결국 이 모든 건 정보의 relation 파악과 검색 효율 향상을 위해 공부하는 것이다
'''
# 개념 이해 완료



# 해시 구현을 어떻게 하는지 모르겠으니 일단 코드 따라쳐 보고 해석하기

def polyhash(str):   # 문자열 해싱 공식 적용하기
    p = 31   # 소수를 설정, 해시 함수의 기본 값으로 사용, 충돌을 줄이는 데에 도움
    m = 1_000_000_007   # 해시 값을 특정 범위 내로 제한하기 위해 버킷의 크기 설정, 큰 소수로 선정하여 해시 충돌 최소화
    hash_value = 0   # 해시 값을 저장할 변수를 초기화, 코드를 돌면서 계산된 해시 값을 저장

    for char in str:   # 문자열의 각 문자를 하나씩 순회
        hash_value = (hash_value * p + ord(char)) % m   # 문자열 해싱에는 문자의 아스키코드 값이 필요함, mod m은 해시값이 m을 넘지 않도록 하기 위한 연산

    return hash_value   # 최종 해시값 반환

def solution(string_list, query_list):
    # 리스트 컴프리헨션 : string_list의 각 문자열에 polyhash 함수를 적용한 결과값을 리스트에 저장
    hash_list = [polyhash(str) for str in string_list]   # polyhash 함수를 이용해 string_list의 각 문자열에 대한 해시 값 계산
    
    result = []   # 결과 저장
    for query in query_list:   # query_list의 각 문자열을 하나씩 순회
        query_hash = polyhash(query)   # 현재 순회 중인 query 문자열에 대해 polyhash 함수의 해시값 계산
        if query_hash in hash_list:   # 이전 라인의 결과값이 hash_list에 있는지 확인
            result.append(True)   # query_hash값이 hash_list에 있으면 result 리스트에 Ture를 추가
        else:
            result.append(False)   # 없으면 False 추가
        
    return result   # 쿼리가 string_list에 있는지 비교한 결과를 반환



'''
해시 함수를 사용해 효율적인 문자열 비교 가능
'''


'''
1. 해시 구현
2. 문자열에 대해 해시값 계산
3. 해시값이 hash table에 있는지 확인
4. 존재하면 true, 아니면 false
'''


# Q : 딕셔너리랑 해시랑 차이점은 단지 메모리 효율 뿐인가?