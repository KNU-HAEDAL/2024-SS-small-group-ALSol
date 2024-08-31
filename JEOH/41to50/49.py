def dfs(cur_k, ent, dungeons, visited): 
    answer_max = ent
    for i in range(len(dungeons)):
        if cur_k >= dungeons[i][0] and visited[i] == 0:
            visited[i] = 1 
            answer_max = max(
            answer_max, dfs(cur_k - dungeons[i][1], ent + 1, dungeons, visited)
            )
            visited[i] = 0 
    return answer_max
def solution(k, dungeons):
    visited = [0] * len(dungeons) 
    answer_max = dfs(k, 0, dungeons, visited) 
    return answer_max