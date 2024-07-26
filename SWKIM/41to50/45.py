# 방문 여부가 이닌 최소 비용을 기준으로 탐색해야 하는 문제

from collections import deque

# 방문 가능한 곳인지 확인하는 함수
def is_move(board, x, y, size):
    if ((x > -1 and x < size) and
        (y > -1 and y < size) and 
        board[x][y] == 0):
        return True
    return False

def solution(board):
    queue = deque()
    movement = [[1, -1, 0, 0], [0, 0, 1, -1]] # 상하좌우 이동
    size = len(board)
    # graph: 각 노드에서 이동방향에 따른 비용을 넣을 수 있도록 함
    # ==> 서로 다른 path에서 다시 만나 이동할 때 직진하거나 코너를 돌 때 최소비용이 역전될 수 있기 때문
    graph = [[[float("inf") for _ in range(4)] for _ in range(size)] for _ in range(size)]

    queue.append([0, 0, -1, 0]) # x, y, state, cost
    graph[0][0] = [0, 0, 0, 0]

    while queue:
        x, y, state, cost = queue.popleft()
        
        # 처음 시작할 때
        if state == -1:
            for i in range(4):
                dx = x + movement[0][i]
                dy = y + movement[1][i]
                
                if is_move(board, dx, dy, size):
                    queue.append([dx, dy, i, cost + 100])
                    graph[dx][dy][i] = cost + 100
        else:
            for i in range(4):
                dx = x + movement[0][i]
                dy = y + movement[1][i]

                if is_move(board, dx, dy, size):
                    if i == state:  # 직진하는 경우
                        graph[dx][dy][i] = min(cost + 100, graph[dx][dy][i]) # 해당 이동방향과 비용 비교

                        # 해당 이동방향의 최소비용이 변경되었고 해당 노드의 최소비용 + 500보다 작다면 큐에 추가
                        # 최소비용 + 500의 의미는 이후 이동방향에 따라 비용이 바뀔 수 있는 최소조건이다.
                        if graph[dx][dy][i] == cost + 100 and cost + 100 < min(graph[dx][dy]) + 500:
                            queue.append([dx, dy, i, cost + 100])                
                    else:   # 코너를 도는 경우
                        graph[dx][dy][i] = min(cost + 600, graph[dx][dy][i])

                        if graph[dx][dy][i] == cost + 600 and cost + 600 < min(graph[dx][dy]) + 500:
                            queue.append([dx, dy, i, cost + 600])                
    
    return min(graph[size-1][size-1]) # 도착지점의 최소비용 반환


board = [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]
print(solution(board))