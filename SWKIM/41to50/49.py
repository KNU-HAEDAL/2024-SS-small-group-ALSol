# 백트래킹을 이용한 깊이 우선탐색(dfs)
def backtrack(dungeons ,visited, cur, cnt):
    max_cnt = cnt
    for i in range(len(dungeons)):
        # 아직 방문하지 않았고 현재 피로도가 최소필요 피로도보다 크다면 이동
        if cur >= dungeons[i][0] and visited[i] == 0:
            visited[i] = 1
            max_cnt = max(max_cnt, backtrack(dungeons, visited, cur - dungeons[i][1], cnt+1))
            visited[i] = 0  # 방문 초기화
    
    return max_cnt
            
def solution(k, dungeons):
    visited = [0 for _ in range(len(dungeons))]

    answer = backtrack(dungeons, visited, k, 0)
    return answer

k = 80
d = [[80, 20], [50, 40], [30, 10]]
print(solution(k, d))




