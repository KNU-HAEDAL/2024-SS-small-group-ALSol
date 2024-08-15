"""
N명의 참가자에게 1부터 N번의 번호를 차례로 배정
1vs2 3vs4 ... N-1 vs N 해서 이기면 다음 라운드 진출
다음 라운드 진출자들 다시 번호 매김
N : 2^1 이상 2^20 이하인 자연수 (2의 지수로 주어지므로 부전승 X)
A, B : N 이하인 자연수 (A != B)
"""
def solution(N, A, B):
    round_num = 1
    while A != B:
        A = (A + 1) // 2
        B = (B + 1) // 2
        round_num += 1
    return round_num - 1

N = 8
A = 4
B = 7
print(solution(N, A, B))
# answer = 3
# 1 -> 1, 2 -> 1, 3 -> 2, 4 -> 2
# 5 -> 3, 6 -> 3, 7 -> 4, 8 -> 4