def solution(arr, n):
    size = len(arr)
    
    # 시계방향으로 90도 돌리는 함수
    def rotate(arr):
        rotated_arr = [[0 for _ in range(size)] for _ in range(size)]

        for x in range(size):
            for y in range(size):
                rotated_arr[y][size - x - 1] = arr[x][y]
        
        return rotated_arr
    
    answer = arr.copy()
    # n번 만큼 회전시킴 
    for _ in range(n):
        answer = rotate(answer)
    
    return answer

arr = [[1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10,11,12],
    [13,14,15,16]]
print(solution(arr, 1))