def solution(keyinput, board):
    answer = [0, 0]
    
    x = board[0] // 2
    y = board[1] // 2
    for key in keyinput:
        # 해당 방향키로 이동이 가능하다면 이동
        if key == 'up' and answer[1] < y: 
            answer[1] += 1
        elif key == 'down' and answer[1] > -1 * y:
            answer[1] -= 1
        elif key == 'right' and answer[0] < x:
            answer[0] += 1
        elif key == 'left' and answer[0] > -1 * x:
            answer[0] -= 1

    return answer

        
