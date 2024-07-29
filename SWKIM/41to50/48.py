# 가로줄에 넣으려는 숫자가 있는지 찾는 함수
def is_row(board, x, num):
    for i in range(9):
        if board[x][i] == num:
            return True
    
    return False

# 세로줄에 넣으려는 숫자가 있는지 찾는 함수
def is_col(board, y, num):
    for i in range(9):
        if board[i][y] == num:
            return True
    
    return False
# 박스 안에 넣으려는 숫자가 있는지 찾는 함수
def is_square(board, x, y, num):
    row = 3 * (x // 3)
    col = 3 * (y // 3)

    for i in range(row, row+3):
        for j in range(col, col+3):
            if board[i][j] == num:
                return True
    
    return False

# 가장 가까운 빈칸을 찾는 함수
def find_empty_node(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j

    return None

# 백트래킹 함수, 재귀적으로 사용한다
def backtrack(board):
    pos = find_empty_node(board)
    
    # 빈칸이 없다면 true, 아니면 빈칸에 숫자를 넣는다.
    if not pos:
        return True
    else:
        x, y = pos
        
        # 빈칸에 숫자를 넣어보고 가능한지 확인한다.
        for num in range(1, 10):
            # 넣을 수 있는 숫자를 찾는다
            if (not is_row(board, x, num) and
                not is_col(board, y, num) and
                not is_square(board, x, y, num)):
                board[x][y] = num

                # 숫자를 넣었을 때 스도쿠가 이상이 없다면
                if backtrack(board):
                    return True
        
        board[x][y] = 0
        # 스도쿠가 정상적으로 완성할 수 없다면 False
        return False

def solution(board):
    backtrack(board)
    return board

b = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0,0,0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0]]

print(solution(b))
