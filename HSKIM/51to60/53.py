def is_valid_move(board, x, y):
    # 현재 위치가 board 안에 있으며, 그 위치가 1인 경우 True 반환
    return 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == 1

def dfs(board, player_pos, opponent_pos, move_count):
    x, y = player_pos

    # 현재 위치가 0이라면 움직일 수 없으므로 종료
    if board[x][y] == 0:
        return move_count

    # 이기는 경우와 지는 경우의 값을 저장하기 위한 리스트
    winning_moves = []
    losing_moves = []

    # 이동 가능한 방향들: 상, 하, 좌, 우
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    can_move = False

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        # 이동이 가능한 위치라면
        if is_valid_move(board, nx, ny):
            can_move = True

            # 현재 위치를 0으로 바꾸어 방문 처리
            board[x][y] = 0

            # 상대방의 결과를 가져옴
            result = dfs(board, opponent_pos, [nx, ny], move_count + 1)

            # 원래 상태로 복구
            board[x][y] = 1

            # 현재 플레이어가 이길 수 있는 경우를 분류
            if result % 2 == move_count % 2:
                losing_moves.append(result)
            else:
                winning_moves.append(result)

    # 이동할 수 없는 경우, 현재 움직임을 반환
    if not can_move:
        return move_count

    # 이길 수 있는 경우가 있다면, 최소 이동을 반환
    if winning_moves:
        return min(winning_moves)
    else:
        # 이길 수 있는 경우가 없다면, 최대 이동을 반환
        return max(losing_moves)

def solution(board, aloc, bloc):
    return dfs(board, aloc, bloc, 0)

board = [[1, 1, 1, 1, 1]]
aloc = [0, 0]
bloc = [0, 4]
print(solution(board, aloc, bloc))  
