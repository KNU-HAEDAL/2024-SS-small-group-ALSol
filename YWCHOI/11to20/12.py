# print("10에 계속 modified 표시 뜨는데 좀 무섭네요..") #test push
# p.153

'''
def solution(prices):
    stock_length = len(prices)
    result_list = []

    for i in range(prices):
        for j in range(i, stock_length):
            if i > prices[j]:
                result_list[i] = j
                continue
    
    return result_list


prices = [1, 2, 3, 2, 3]
print(solution(prices))
'''

def solution(prices):
    stock_length = len(prices)
    result_list = []

    for i in range(stock_length - 1):
        count = 0
        for j in range(i + 1, stock_length):
            count += 1
            if prices[i] > prices[j]:
                break
        result_list.append(count)

    result_list.append(0)
    
    return result_list


prices = [1, 2, 3, 2, 3]
print(solution(prices))