import heapq

# 힙 정렬을 통해 문제 헤결

# 이동 가능한 곳인지 판단하는 함수
def is_move(x, y, size):
    if ((x > -1 and x < size) and
        (y > -1 and y < size)):
            return True
    else: 
        return False

def solution(land, height):
    answer = 0
    size = len(land)
    movement = [[1,-1,0,0],[0,0,1,-1]]
    visited = [[False for _ in range(size)] for _ in range(size)]
    heap = []
    heapq.heappush(heap, (0, 0, 0)) # cost, x, y


    while heap:
        cost, x, y = heapq.heappop(heap)

        # 방문하지 않은 곳인 경우
        if not visited[x][y]:
            visited[x][y] = True
            answer += cost  # cost 추가

            # 상하좌우로 이동
            for i in range(4):
                dx = x + movement[0][i]
                dy = y + movement[1][i]
                
                if is_move(dx, dy, size):
                    temp_cost = abs(land[dx][dy] - land[x][y])

                    # 사다리가 필요한지 판단하여 힙에 추가
                    # 이때 cost가 낮은 순으로 정렬이 된다
                    if temp_cost <= height:
                        heapq.heappush(heap, (0, dx, dy))
                    else:
                        heapq.heappush(heap, (temp_cost, dx, dy))     
            
    return answer

land = [[1, 4, 8,10], [5, 5, 5, 5], [10,10,10,10], [10,10,10, 20]]
height = 3
print(solution(land, height))
