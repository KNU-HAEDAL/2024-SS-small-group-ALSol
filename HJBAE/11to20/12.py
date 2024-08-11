#12번
#초 단위로 기록된 주식 가격이 담긴 배열 prices
#가격이 떨어지지 않은 기간은 몇 초인지 반환하는 solution() 함수

def solution(prices):
    answer = []

    for i in range(len(prices)):
        count = 0
        for j in range(i + 1, len(prices)):
            count += 1
            if prices[i] > prices[j]:
                break
        answer.append(count)
    return answer

prices = [1, 2, 3, 2, 3]
print(solution(prices))

"""
2초 [1, 0, 0, 0, 0]
3초 [2, 1, 0, 0, 0]
4초 [3, 2, 1, 0, 0]
5초 [4, 3, 1, 1, 0]
"""
