# 현재 위치가 이동 가능한 위치인지 확인하는 함수
def move(board, x_length, y_length, x, y, competitor):
    # 현재 위치가 board 안에 있으며 현재 위치가 1이라면 True, 아니라면 False 반환
    if ((x > -1 and x < x_length) and
        (y > -1 and y < y_length) and
        (board[x][y] == 1)):
        return True
    return False

def solution(board, aloc, bloc):
    movement = [[1, -1, 0, 0], [0, 0, 1, -1]]
    x_length = len(board)
    y_length = len(board[0])
    answer = -1

    # 1) 현재 플래이어가 이기는 경우가 하나라도 있다면 이기는 경우의 수 중 최솟값 선택
    # 2) 현재 플래이어가 이기는 경우가 없다면 지는 경우의 수 중 최댓값 선택
    # 위 두가지를 고려하여 함수를 만들어야 함
    def dfs(cnt, player, competitor, answer):
        x, y = player
        
        # 현재 위치가 0인 경우
        if board[x][y] == 0:
            return cnt
        
        # 이기는 경우와 지는 경우의 값을 저장하기 위한 리스트
        win_data = []
        lose_data = []

        check = True    # 움직일 수 있는 발판이 하나라도 있다면 False

        # 상하좌우 이동
        for i in range(4):
            dx = x + movement[0][i]
            dy = y + movement[1][i]

            # 이동이 가능한 위치라면
            if move(board, x_length, y_length, dx, dy, competitor):
                check = False

                board[x][y] = 0                
                player = [dx, dy]
                result = dfs(cnt+1, competitor, player, answer)
                
                # 현재 플레이어가 1번 플레이어인 경우
                if cnt % 2 == 0:
                    # reuslt가 홀수면 승리, 아니하면 패배
                    if result % 2 == 1:
                        win_data.append(result)
                    else:
                        lose_data.append(result)
                else:   # 현재 플레이어가 2번 플레이어인 경우
                    # result가 짝수면 승리, 아니면 패배
                    if result % 2 == 1:
                        lose_data.append(result)
                    else:
                        win_data.append(result)             
 
                board[x][y] = 1
        
        if check:   # 이동할 수 없는 위치인 경우    
            return cnt
        elif win_data:  # 이긴 경우가 하나라도 있는 경우
            return min(win_data)    # 이긴 경우 중 최솟값 반환
        else:   # 무조건 지는 경우
            return max(lose_data)   # 지는 경우 중 최댓값 반환
                
    answer = dfs(0, aloc, bloc, answer)
    return answer


board = [[1]]
aloc = [0,0]
bloc = [0,0]
print(solution(board, aloc, bloc))
