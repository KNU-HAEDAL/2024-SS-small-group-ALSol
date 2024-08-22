from itertools import combinations

# 유저 아이디와 제재 아이디가 동일한지 비교
def compare(id, banned_id):
    if len(id) == len(banned_id):
        for i in range(len(id)):
            if banned_id[i] != '*' and id[i] != banned_id[i]:
                return False
        return True
    return False

def solution(user_id, banned_id):
    answer = 0
    size = len(banned_id)

    # 조합으로 제재 아이디와 동일한지 비교
    combi = list(combinations(user_id, size))

    for people in combi:
        visited = [False]*size

        # 가능한 모든 경우를 탐색하면서 제재 아이디와 동일한 경우 true
        def dfs(idx, visited):
            if idx == size: # 모든 아이디가 제재 아이디와 같은 경우 true
                return True
            
            result = False
            user = people[idx]

            # 방문하지 않은 제재 아이디들을 방문
            for i in range(size):
                if not visited[i]:
                    # 비교를 통해 동일하다면 방문
                    if compare(user, banned_id[i]):
                        visited[i] = True    

                        if dfs(idx+1, visited):
                            return True
                        visited[i] = False
                                        
            return False    # 비교를 통해 동일하지 않다면 false
        
        if dfs(0, visited): # 동일한 경우 +1
            answer += 1
        
    return answer

print(solution(	["frodo", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))