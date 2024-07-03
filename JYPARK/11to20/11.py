def solution(prices):
    length = len(prices)
    answer = [0] * length
    
    for i in range(length):
        count = 0
        for j in range(i, length):
            if prices[i] <= prices[j]:
                count += 1
        answer[i] = count-1

    return answer

prices = input().strip('[]')
prices = list(map(int, prices.split(', ')))
print(solution(prices))