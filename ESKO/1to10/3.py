def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            sum = numbers[i] + numbers[j]
            answer.append(sum)

    res = list(set(answer))
    res.sort()
    return res