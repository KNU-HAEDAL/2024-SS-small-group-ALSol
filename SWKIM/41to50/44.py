from collections import deque

def solution(N, road, K):
    distance = [float("inf") for _ in range(N)]
    answer = set()
    graph = {start: {} for start in range(1, N + 1)}    # key: 출발지, value: 도착지와 거리
    queue = deque()
    distance[0] = 0
    queue.append([1, 1, 0])

    # value 값에서 더 낮은 거리를 값으로 가지도록 함
    for start, end, weight in road:
        if end in graph[start]:
            graph[start][end] = min(weight, graph[start][end])
            graph[end][start] = min(weight, graph[start][end])
        else:
            graph[start][end] = weight
            graph[end][start] = weight
        
    while queue:
        past, cur, cnt = queue.popleft()
        answer.add(cur)

        # 이전에 방문한 곳이 아니며 K 값 이내이면서 최단거리일 때 큐에 저장
        for town in graph[cur]:
            if town != past and cnt + graph[cur][town] <= K:
                if cnt + graph[cur][town] < distance[town - 1]:
                    distance[town - 1] = cnt + graph[cur][town]
                    queue.append([cur, town, cnt + graph[cur][town]])
                


    return len(answer)


N = 5
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3
print(solution(N, road, K))