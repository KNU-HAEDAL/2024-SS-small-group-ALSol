def solution(arr):
    unique_arr = list(set(arr))
   
    unique_arr.sort(reverse=True)
    return unique_arr

arr = [3, 2, 1, 2, 4]

result = solution(arr)

print(result) 
