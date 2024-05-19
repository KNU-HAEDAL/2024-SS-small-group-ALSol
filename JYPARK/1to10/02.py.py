#문제02
def solution(arr):
    result = list(set(arr)) #중복제거, 오름차순정리
    result = result.sort(reverse = True)
    return result