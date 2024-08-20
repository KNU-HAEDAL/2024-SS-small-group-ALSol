"""
N마리의 포켓몬 중 N / 2마리 가져가도 좋다고 함
같은 종류의 포켓몬 -> 같은 번호를 가짐
4마리 포켓몬 있는데 각각 [3번, 1번, 2번, 3번]이면
1번 포켓몬 1마리, 2번 포켓몬 1마리, 3번 포켓몬 2마리
최대한 많은 종류의 포켓몬을 얻을 수 있는 N / 2 마리 선택하려고 함
solution() = 가장 많은 종류의 포켓몬을 찾아 선택하는 방법 -> 종류 번호의 개수 반환
"""
def solution(nums):
    n = len(set(nums))
    k = int(len(nums) / 2)
    if k <= n:
        return k
    else:
        return n

nums1 = [3, 1, 2, 3]
# result = 2 -> 2마리 골라야 하고 3종류 선택지 있음 n = 3, k = 2
nums2 = [3, 3, 3, 2, 2, 4]
# result = 3 -> 3마리 골라야 하고 3종류 선택지 있음 n = 3, k = 3
nums3 = [3, 3, 3, 2, 2, 2]
# result = 2 -> 3마리 골라야 하고 2종류 선택지 있음 n = 2, k = 3
print(solution(nums1))
print(solution(nums2))
print(solution(nums3))