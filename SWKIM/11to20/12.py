def solution(prices):
    n = len(prices)
    idxStack = []
    times = [0 for _ in range(n)]

    for i in range(n):
        while True:
            if not idxStack or prices[idxStack[-1]] <= prices[i]:
                idxStack.append(i)
                break
            
            idx = idxStack.pop()
            times[idx] = i - idx


    for i in idxStack:
        times[i] = n-i-1
    
    return times

