from collections import Counter
def solution(k, tangerine):
    counter = Counter(tangerine)
    sorted_counts = sorted(counter.values(), reverse=True)
    num = 0 
    sum = 0
    for count in sorted_counts: 
        sum += count 
        num_types += 1
        if sum >= k:
            break
    return num