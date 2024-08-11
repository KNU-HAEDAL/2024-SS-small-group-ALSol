def solution(n):
    arr = [[0]*n for _ in range(n)]
    num = 2
    # 달팽이 그림처럼 이동하는 2차원 배열
    movement = [[1, 0, -1, 0], [0, 1, 0, -1]]
    pos = 0 # 움직이는 방향을 결정하는 변수
    x = 0
    y = 0
    arr[0][0] = 1

    # n*n번 만큼 반복
    while num <= n * n:
        # 움직임 결정
        for i in range(4):
            # pos%4를 통해 움직이는 방향 결정
            dx = x + movement[0][pos%4]
            dy = y + movement[1][pos%4]
            # 이동 가능한 경우
            if -1 < dx < n and -1 < dy < n and arr[dx][dy] == 0:
                x = dx
                y = dy
                arr[x][y] = num
                num += 1
                break
            # 이동할 수 없는 경우
            else:
                pos += 1    # 움직이는 방향 수정

    return arr

print(solution(5))