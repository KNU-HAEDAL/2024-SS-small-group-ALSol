def solution(arr, target):
    #해시 테이블 생성
    hashtable = [0] * (target + 1)
    for num in arr:
        if num <= target:
            hashtable[num] = 1
    for num in arr:
        x = target - num
        if hashtable[x] == 1 and x != num and x <= target and x >= 0:
            answer = 'True'
            break
        else:
            answer = 'False'
    return answer


arr = [1, 2, 3, 4, 8]
target = 8
print(solution(arr, target))