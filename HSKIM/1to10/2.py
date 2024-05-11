def solution(arr):
    result = arr(set(arr))
    result.sort(reverse=True)
    
    return result