def solution(numbers):
    sum = []
    num = 0
    l = len(numbers)

    for i in range(0, l):
        for j in range(0, l):
            num = numbers[i] + numbers[j]
            if i != j: 
                sum.append(num)
    lst = list(set(sum))
    return lst