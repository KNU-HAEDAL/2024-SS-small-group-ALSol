def solution(arr1, arr2):
    answer=[[]]
    a1,a10=len(arr1),len(arr1[0])
    a2,a20=len(arr2),len(arr2[0])
    answer=[[0]*a20 for _ in range(a1)]
    for i in range(a1):
        for k in range(a20):
            for q in range(a2):
                answer[i][k]+=arr1[i][q]*arr2[q][k]       
    return answer