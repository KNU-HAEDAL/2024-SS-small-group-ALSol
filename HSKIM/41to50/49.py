# 백트래킹을 이용한 깊이 우선탐색(dfs)
def dfs(cur, cnt, dungeons, visited):
    answer_max = cnt
    for i in range(len(dungeons)):
        need = dungeons[i][0]
        used = dungeons[i][1]
        if cur >= need and visited[i] == 0:
            visited[i] = 1

            answer_max = max(answer_max, dfs(cur - used, cnt + 1, dungeons, visited))
            visited[i] = 0
    
    return answer_max

def solution(k, dungeons):
    visited = [0] * len(dungeons)
    answer_max = dfs(k, 0, dungeons, visited)

    return answer_max

k = 80
d = [[80, 20], [50, 40], [30, 10]]
print(solution(k, d))