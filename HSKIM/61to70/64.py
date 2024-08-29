def solution(n):
    arr = [[0] * n for _ in range(n)]
    num = 1
    # 달팽이 그림처럼 이동하는 2차원 배열
    movement = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x, y = 0, 0
    direction = 0  # 초기 방향은 오른쪽(우)

    # n * n번 만큼 반복
    while num <= n * n:
        arr[x][y] = num
        num += 1

        # 다음 위치 계산
        dx, dy = x + movement[direction][0], y + movement[direction][1]

        # 이동이 가능한 경우
        if 0 <= dx < n and 0 <= dy < n and arr[dx][dy] == 0:
            x, y = dx, dy
        else:
            # 이동할 수 없는 경우 방향을 변경
            direction = (direction + 1) % 4
            x += movement[direction][0]
            y += movement[direction][1]

    return arr

print(solution(3))
