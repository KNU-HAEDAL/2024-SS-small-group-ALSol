def solution(keyinput, board):
    # 방향에 따른 이동 변화량 설정
    move = {
        'up': (0, 1),
        'down': (0, -1),
        'left': (-1, 0),
        'right': (1, 0)
    }
    
    # 초기 위치 설정
    position = [0, 0]
    
    # 최대 이동 가능한 범위 계산
    max_x = board[0] // 2
    max_y = board[1] // 2
    
    for key in keyinput:
        dx, dy = move[key]  # 이동 변화량 가져오기
        # 이동 가능한 범위 내에서만 이동
        if -max_x <= position[0] + dx <= max_x:
            position[0] += dx
        if -max_y <= position[1] + dy <= max_y:
            position[1] += dy
    
    return position

print(solution(["left", "right", "up", "right", "right"], [11, 11]))  
