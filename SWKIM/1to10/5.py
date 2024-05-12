def solution(arr1, arr2):
    answer = list([0 for j in range(len(arr2[0]))] for i in range(len(arr1)))


    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            data = 0
            for k in range(len(arr2)):
                data += arr1[i][k] * arr2[k][j]
            
            answer[i][j] = data
    
    return answer



