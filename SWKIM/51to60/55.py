def solution(arr1, arr2):
    answer = []
    pointer1 = 0
    pointer2 = 0

    # 두 배열을 순회하면서 오름차순 정렬 실행
    while pointer1 < len(arr1) and pointer2 < len(arr2):
        if arr1[pointer1] < arr2[pointer2]:
            answer.append(arr1[pointer1])
            pointer1 += 1
        else:
            answer.append(arr2[pointer2])
            pointer2 += 1

    # 아직 남은 값들을 추가
    while pointer1 < len(arr1):
        answer.append(arr1[pointer1])
        pointer1 += 1

    while pointer2 < len(arr2):
        answer.append(arr2[pointer2])
        pointer2 += 1

    return answer

print(solution([1,2,3], [4,5,6]))