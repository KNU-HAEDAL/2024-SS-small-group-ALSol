def solution(d, budget):
    d.sort() 
    count = 0 
    for amount in d:
        if budget < amount:
            break
        budget -= amount 
        count += 1
    return count if budget >= 0 else count - 1