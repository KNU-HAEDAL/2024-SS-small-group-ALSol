# 푸는데 3일 걸린 레전드 문제
# 큐에 넣기 전 해당 위치를 방문했다고 표시해야 하는데
# 큐에서 꺼낸 후 방문했다고 표시해서 시간 초과가 났다.

# 큐를 활용해 이동할 곳 찾음
from collections import deque

# 현재 위치가 maps 내에 있고 X가 아니라면 True
def move(maps, row, col, x, y):
    if ((x >= 0 and x < row) and 
        (y >= 0 and y < col)):

        if maps[x][y] != 'X':
            return True

    return False


def solution(maps):
    answer = 0
    start = False   # start에서 lebber까지 이동완료하면 True
    lebber = False  # lebber에서 exit까지 이동완료하면 True
    row = len(maps)
    col = len(maps[0])

    # start에서 시작할 때와 lebber에서 시작할 때 사용할 maze
    # lebber에 도착하기까지 방문한 곳을 중복하여 방문 할 수 있도록 하기 위함
    maze1 = [[False for _ in range(col)] for _ in range(row)]   
    maze2 = [[False for _ in range(col)] for _ in range(row)]

    # 상하좌우 이동
    movement = [[1, -1, 0, 0], [0, 0, -1, 1]]
    
    # start에서 lebber까지 이동하는 큐와 lebber에서 exit까지 이동하는 큐
    start_to_lebber = deque()
    lebber_to_exit = deque()

    # maps에서 start와 lebber의 위치를 찾아 큐에 넣기
    for i in range(row):
        for j in range(col):
            if maps[i][j] == 'S':
                maze1[i][j] = True
                start_to_lebber.append([i, j, 0])
            elif maps[i][j] == 'L':
                maze2[i][j] = True
                lebber_to_exit.append([i, j, 0])

    while True:
        # lebber나 exit에 도달하지 못하는 경우
        if ((len(start_to_lebber) == 0 and not start) or
            len(lebber_to_exit) == 0 and not lebber):
            answer = -1
            break
        
        # lebber를 거쳐 exit까지 도달한 경우
        if start and lebber:
            break

        # lebber에 도달하지 못했다면
        if not start:
            point = start_to_lebber.popleft()

            # 상하좌우로 이동
            for i in range(4):
                x = point[0] + movement[0][i]
                y = point[1] + movement[1][i]

                # 이동 가능하다면 
                if move(maps, row, col, x, y):
                    if maps[x][y] == 'L':
                        start = True
                        answer += point[2] + 1
                    elif not maze1[x][y]:
                        maze1[x][y] = True
                        start_to_lebber.append([x, y, point[2]+1])

        # lebber에 도달했고 exit에 도달하지 못했다면
        elif start and not lebber:
            point = lebber_to_exit.popleft()

            for i in range(4):
                x = point[0] + movement[0][i]
                y = point[1] + movement[1][i]

                if move(maps, row, col, x, y):
                    if maps[x][y] == 'E':
                        lebber = True
                        answer += point[2] + 1
                    elif not maze2[x][y]:
                        maze2[x][y] = True
                        lebber_to_exit.append([x, y, point[2]+1])


    return answer

maps = ["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]
print(solution(maps))

