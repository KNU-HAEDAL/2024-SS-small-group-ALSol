from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    dist = [[-1 for _ in range(m)] for _ in range(n)]           #걸리는 시간을 저장할거임. 일단 -1로 초기화
    dist[0][0] = 1
    q = deque([[0, 0]])             #[0, 0]가 담긴 리스트 생성
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <=nx <m and 0 <=ny <n and maps[ny][nx] != 0 and dist[ny][nx] == -1:         #범위 내이고, 벽이 아니고, 방문하지 않은 칸이라면
                q.append([ny, nx])
                dist[ny][nx] = dist[y][x] + 1
            if ny == n-1 and nx == m-1:
                return dist[n-1][m-1]
            
    return -1

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
#maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
print(solution(maps))