from collections import Counter
def solution(topping):
    cnt = 0
    topping_counter = Counter(topping)
    half_topping_set = set()
    for t in topping:
        half_topping_set.add(t) 
        topping_counter[t] -= 1
        if topping_counter[t] == 0: 
            topping_counter.pop(t)
        if len(half_topping_set)==len(topping_counter):
            cnt+=1
    return cnt
