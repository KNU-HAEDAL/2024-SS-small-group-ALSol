def solution(amount):
  denominations = [1, 10, 50, 100]
  denominations.sort(reverse=True) 
  change = [] 
  for coin in denominations:
    while amount >= coin: 
        change.append(coin) 
        amount -= coin  
  return change
