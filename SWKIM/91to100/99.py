def solution(board, skill):
    answer = 0

    # 누적합 활용을 위한 배열
    matrix = [[0 for _ in range(len(board[0])+1)]for _ in range(len(board) + 1)]

    while skill:
        t, x, y, r, c, num = skill.pop()

        # (x, y) / (r+1, y) / (x, c+1) / (r+1, c+1)에 
        # 주어진 타입에 따라 숫자를 넣음
        if t == 1:
            matrix[x][y] -= num
            matrix[r+1][y] += num
            matrix[x][c+1] += num
            matrix[r+1][c+1] -= num
        else:
            matrix[x][y] += num
            matrix[r+1][y] -= num
            matrix[x][c+1] -= num
            matrix[r+1][c+1] += num
    
    # 누적합 열 방향
    for i in range(len(matrix)):
        for j in range(1, len(matrix[0])):
            matrix[i][j] += matrix[i][j-1]

    # 누적합 행 방향
    for i in range(len(matrix[0])):
        for j in range(1, len(matrix)):
            matrix[j][i] += matrix[j-1][i]

    # 비교를 통해 부서지지 않은 것 갯수 확인
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] + matrix[i][j] > 0:
                answer += 1
    
    return answer

print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))