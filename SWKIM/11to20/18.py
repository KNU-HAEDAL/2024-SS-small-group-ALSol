def solution(arr, target):
    hashtable = [0 for _ in range(target+1)]
    
    # arr에 존재하는 데이터를 해쉬 테이블의 인덱스로 하여 값을 1로 설정
    for i in arr:
        if i <= target:
            hashtable[i] = 1
    
    for i in arr:
        num = target - i

        # 아래 조건에 만족하면 arr에 있는 서로 다른 두 숫자의 합이 target을 만족함
        if (num > 0 
            and num < target
            and i != num
            and hashtable[num] == 1):
            return True
   
    return False

print(solution([1,2,3,4,8], 6))
