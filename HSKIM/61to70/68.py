def solution(n):
    return bin(n).count('1') # 2진수로 변환하고 1의 개수를 반환

print(solution(5000))