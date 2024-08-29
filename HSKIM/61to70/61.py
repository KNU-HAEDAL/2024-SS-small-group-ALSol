import heapq

def is_valid_position(x, y, size):
    # x, y가 유효한 범위 내에 있는지 확인
    return 0 <= x < size and 0 <= y < size

def solution(land, height):
    answer = 0
    size = len(land)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 이동 방향: 하, 상, 우, 좌
    visited = [[False] * size for _ in range(size)]
    heap = [(0, 0, 0)]  # 초기 위치: (비용, x, y)

    while heap:
        cost, x, y = heapq.heappop(heap)

        if not visited[x][y]:
            visited[x][y] = True
            answer += cost  # 최소 비용을 결과에 추가

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if is_valid_position(nx, ny, size):
                    # 현재 위치와 다음 위치의 높이 차이를 계산
                    height_diff = abs(land[nx][ny] - land[x][y])

                    # 높이 차이가 주어진 height 이하이면 추가 비용 없이 이동
                    if height_diff <= height:
                        heapq.heappush(heap, (0, nx, ny))
                    else:
                        # 높이 차이가 height를 초과하면 그 차이를 비용으로 추가
                        heapq.heappush(heap, (height_diff, nx, ny))

    return answer

land = [[1, 4, 8, 10], 
        [5, 5, 5, 5], 
        [10, 10, 10, 10], 
        [10, 10, 10, 20]]
height = 3

print(solution(land, height))  
