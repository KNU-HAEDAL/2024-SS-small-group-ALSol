def solution(array, commands):
    answer = []

    for i, j, idx in commands:
        arr = array[i-1: j]
        arr.sort()
        answer.append(arr[idx-1])
    
    return answer

array = [1,5,2,6,3,7,4]
commands = [[2,5,3],[4,4,1],[1,7,3]]
print(solution(array, commands))
