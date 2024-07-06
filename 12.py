def solution(prices):
    length = len(prices)
    stack = [0]
    top = 0
    result = [0] * length


    for i in range (1, length):
        while stack and prices[i] < prices[stack[-1]]:
           a = stack.pop()
           result[a] = i - a
        
        stack.append(i)
       
    while stack:
        a = stack.pop()
        result[a] = length - a - 1
    
    return result 

prices = input().strip('[]')
prices = list(map(int, prices.split(', ')))
print(solution(prices))