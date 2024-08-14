def solution(info, edges):
    answer = 0
    n = len(info)

    graph = [[] for _ in range(n)]
    for s, e in edges:
        graph[s].append(e)
        graph[e].append(s)

    visit = [[[0]*(n+1) for _ in range(n+1)] for _ in range(n+1)]
    visit[1][0][0] = 1
    info[0] = -1
    def dfs(sw, now):
        nonlocal answer
        
        if sw[0] > answer:
            answer = sw[0]

        # 늑대 수가 더 많으면 return
        if sw[1] >= sw[0]:
            return

        for node in graph[now]:
            # print(sw, now)

            if visit[sw[0]][sw[1]][node] == 0:

                # 늑대나 양이 있는 경우
                if info[node] != -1:

                    # tmp: 현재 양 또는 늑대
                    tmp = info[node]

                    # 양이면 0에 +1, 늑대면 1에 +1
                    sw[tmp] += 1

                    # 방문처리
                    visit[sw[0]][sw[1]][node] = 1

                    # 데리고 다니니까 -1 처리
                    info[node] = -1
                    dfs(sw, node)

                    # 원래 양 또는 늑대 복구
                    info[node] = tmp

                    # 방문처리 취소
                    visit[sw[0]][sw[1]][node] = 0

                    # 데리고 다니던 양 또는 늑대 반환
                    sw[tmp] -= 1


                # 이미 데리고 다니는 경우
                else:

                    # 현재 상태 방문처리
                    visit[sw[0]][sw[1]][node] = 1
                    dfs(sw, node)
                    # 방문 처리 취소
                    visit[sw[0]][sw[1]][node] = 0

    # 첫 시작 양1마리, 늑대0마리 노드번호 0번 dfs 시작
    dfs([1, 0], 0)

    return answer

#info = [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1]
#edges = [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9,10], [9,11], [4, 3], [6, 5], [4, 6], [8, 9]]
info = [0,1, 0,1,1, 0,1, 0, 0,1, 0]
edges = [[0,1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9,10]]
solution(info, edges)