def solution(numbers):
    answer_set = set()
    
   
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            answer_set.add(numbers[i] + numbers[j])
    
  
    return sorted(list(answer_set))

numbers = [2, 1, 3, 4, 1]

result = solution(numbers)

print(result)  # [2, 3, 4, 5, 6, 7]
