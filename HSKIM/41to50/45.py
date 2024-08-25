from collections import deque

# 방문 가능한 곳인지 확인하는 함수
def is_move(board, x, y, size):
    return 0 <= x < size and 0 <= y < size and board[x][y] == 0

def solution(board):
    size = len(board)
    movement = [[1, -1, 0, 0], [0, 0, 1, -1]]  # 상하좌우 이동
    graph = [[float('inf')] * size for _ in range(size)]
    
    queue = deque([(0, 0, -1, 0)])  # (x, y, 방향, 비용)
    graph[0][0] = 0
    
    while queue:
        x, y, prev_dir, cost = queue.popleft()
        
        for i in range(4):
            dx, dy = x + movement[0][i], y + movement[1][i]
            
            if is_move(board, dx, dy, size):
                new_cost = cost + (100 if i == prev_dir or prev_dir == -1 else 600)
                
                if new_cost < graph[dx][dy]:
                    graph[dx][dy] = new_cost
                    queue.append((dx, dy, i, new_cost))
    
    return graph[-1][-1]  # 도착지점의 최소비용 반환

board = [[0,0,0],
         [0,0,0],
         [0,0,0]]

print(solution(board))  
