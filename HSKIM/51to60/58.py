def solution(array, commands):
    answer = []

    for cmd in commands:
        i, j, k = cmd
        arr = array[i-1 : j] # i번째부터 j번째까지 자르기
        arr.sort()
        answer.append(arr[k - 1])
    
    return answer

array = [1,5,2,6,3,7,4]
commands = [[2,5,3],[4,4,1],[1,7,3]]
print(solution(array, commands))