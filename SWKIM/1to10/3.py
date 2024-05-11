def solution(arr):
    answer = []

    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            answer.append(arr[i]+arr[j])

    
    answer = list(set(answer))
    answer.sort()

    return answer

number1 = [2, 1, 3, 4, 1]
number2 = [5, 0, 2, 7]

print(solution(number1))
print(solution(number2))