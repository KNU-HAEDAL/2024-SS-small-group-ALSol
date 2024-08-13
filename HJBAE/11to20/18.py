"""
n개의 양의 정수로 이루어진 리스트 arr와 정수 target이 주어졌을 때
이 중에서 합이 target인 두 수가 arr에 있는지 찾고
있으면 True, 없으면 False를 반환하는 solution() 함수를 작성

n은 2 이상 10000 이하의 자연수
arr의 각 원소는 1 이상 10000 이하의 자연수
arr의 원소 중 중복되는 원소는 없음
target은 1 이상 20000 이하의 자연수
"""

def count_sort(arr, k):    #target 값이 K로 들어감
    hash_table = [0] * (k + 1)
    #어쨋든 target 값보다 큰 값이 더해져버리면 안되니까 target 값 보다 작으면 그냥 0의 값으로 둬도 됨
    for i in arr:
        if i <= k:
            hash_table[i] = 1
    return hash_table


def solution(arr, target):
    hash_table = count_sort(arr, target)
    # i + minus = target
    for i in arr:
        minus = target - i
        print(minus)
        # 이제 minus에 해당하는 값이 해시테이블 내에 존재하는지 (1인지 판단)
        if ((hash_table[minus] == 1) and (minus != i)):
            return True
    return False
        
arr1 = [1, 2, 3, 4, 8]
target1 = 6
arr2 = [2, 3, 5, 9]
target2 = 10

print(solution(arr1, target1))
print(solution(arr2, target2))

# 뭐임 왜 두번째 True 뜨냐..
"""
2, 3, 5, 9 = 1
10 - 2 = 8
10 - 3 = 7
10 - 5 = 5 <- 얘 같으니까 안되잖아
10 - 9 = 1
"""