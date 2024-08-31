from collections import deque

# 이동 가능한 곳인지 확인하는 함수
def is_move(maps, x, y):
    if ((x > -1 and x < len(maps)) and
        (y > -1 and y < len(maps[0])) and
        (maps[x][y] == 1)):
        return True
    
    return False

def solution(maps):
    queue = deque()
    movement = [[-1, 1, 0, 0], [0, 0, -1, 1]]   # 상하좌우 이동

    queue.append([0, 0, 1])
    maps[0][0] = 0

    while queue:
        x, y, cnt = queue.popleft()

        # 현재 위치에서 상하좌우로 이동
        for i in range(4):
            dx = x + movement[0][i]
            dy = y + movement[1][i]

            if is_move(maps, dx, dy):
                # 도착지점이라면 cnt 리턴
                if dx == len(maps) - 1 and dy == len(maps[0]) - 1:
                    return cnt + 1

                maps[dx][dy] = 0
                queue.append([dx, dy, cnt + 1])

    return -1
    


maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(maps))