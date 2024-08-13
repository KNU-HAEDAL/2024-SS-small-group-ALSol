def solution(arr):
    result_1 = 0
    result_2 = 0

    for i in range(len(arr[0])):
        # 크게 2가지 경우로 결정
        # 1번째 행과 3번째의 수 선택하는 경우 / 1번째 행만 선택하는 경우 / 3번째 행만 선택하는 경우
        # 2번째 행만 선택하는 경우

        # 인접한 경우에는 조약돌을 둘 수 없기에 두가지 경우로 구분
        if i % 2 == 0:
            result_1 += max(arr[0][i], arr[2][i], arr[0][i] + arr[2][i])
            result_2 += arr[1][i]
        else:
            result_2 += max(arr[0][i], arr[2][i], arr[0][i] + arr[2][i])
            result_1 += arr[1][i]

    # 최댓값 반환
    return max(result_1, result_2)

print(solution([[1, 7,13, 2, 6], [2, -4, 2, 5, 4], [5, 3, 5, -3,1]]))