#레버 당김 여부에 따라 visited를 저장하는 것. 그래서 3차원 배열을 사용함. 
#레버 당김여부와 상관없이 2차원으로 visited를 사용했을 때 레버가 안 당겨졌는데도 visited가 True로 변경되어 오류가 발생함

from collections import deque

def solution(maps):
    n = len(maps)               #y좌표
    m = len(maps[0])            #x좌표
    k = 0                       #레버
    q = deque()
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[[False for _ in range(2)]for _ in range(m)] for _ in range(n)]
    flag = False

    #시작, 끝 좌표를 찾을 것임
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':           #시작점인 경우
                q.append((i, j, 0, 0))      #시작좌표를 추가 (y좌표, x좌표, 레버당김여부, 걸린시간)
                visited[i][j][0] = True
                flag = True                 #시작점은 하나이므로 찾았으면 바로 종료해준다
                break
        if flag:
            break

    while q:                                #덱이 살아있는 동안
        y, x, k, time = q.popleft()         #왼쪽에서 팝

        if maps[y][x] == 'E' and k == 1:        #레버가 당겨지고 끝점이라면
            return time

        for i in range(4):                  #dy, dx 사용하려고 4번 반복함
            ny = y + dy[i]
            nx = x + dx[i]                  #현재 위치에서 상하좌우 확인하려고

            if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] != 'X':         #범위 내이고 벽이 아니고 방문했던 곳이 아닌 경우
                    if maps[ny][nx] == 'L':
                        visited[ny][nx][1] = True
                        q.append((ny, nx, 1, time+1))
                    else:
                        if visited[ny][nx][k] != True:
                            visited[ny][nx][k] = True
                            q.append((ny, nx, k, time+1))
    return -1                    #while문을 다 돌았다는 것은 레버당긴채로 끝점까지 못갔다는 뜻.

#maps = ["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]
#maps = ["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]
maps = ["XOOXX", "XOOXX", "XOSOO", "XOXXO", "XOLOE"]
print(solution(maps))