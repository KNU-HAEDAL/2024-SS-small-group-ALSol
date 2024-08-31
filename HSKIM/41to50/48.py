def is_valid(board, x, y, num):
    # 가로줄, 세로줄, 3x3 박스에서 같은 숫자가 있는지 확인
    for i in range(9):
        if board[x][i] == num or board[i][y] == num:
            return False
    
    # 3x3 박스 안에서 같은 숫자가 있는지 확인
    row_start, col_start = 3 * (x // 3), 3 * (y // 3)
    for i in range(row_start, row_start + 3):
        for j in range(col_start, col_start + 3):
            if board[i][j] == num:
                return False
                
    return True

def find_empty_node(board):
    # 빈칸을 찾는다 (0으로 표시된 부분)
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def solve_sudoku(board):
    empty = find_empty_node(board)
    
    if not empty:
        return True  # 모든 빈칸이 채워졌다면 성공
    
    x, y = empty
    for num in range(1, 10):
        if is_valid(board, x, y, num):
            board[x][y] = num
            
            if solve_sudoku(board):
                return True
            
            board[x][y] = 0  # 되돌리기 (백트래킹)
    
    return False  # 모든 경우를 시도해도 안 되면 실패

def solution(board):
    solve_sudoku(board)
    return board

b = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0]]

print(solution(b))
