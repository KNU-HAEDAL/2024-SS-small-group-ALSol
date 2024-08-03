from itertools import permutations
# 순열 사용

def solution(n, weak, dist):
    size = len(weak)
    answer = -1

    # 양방향이 아닌 한쪽 방향으로만 계산을 하기 위함
    for i in range(size):
        weak.append(n+weak[i])

    # 순열을 사용해 사람들이 나오는 다양한 순서 적용
    friend = list(permutations(dist))
    
    # weak의 길이만큼 반복하여 각 weak의 값을 출발지로 함
    for i in range(size):
        # 순열을 통한 다양한 사람들의 나오는 순서
        for j in friend:
            # 한쪽 방향으로의 계산을 위한 방법
            pos = weak[i:i+size]
            j = list(j)
            
            # 백트래킹을 활용한 dfs 함수
            def dfs(pos, start, friend, cnt):
                if len(friend) == 0:
                    return -1
                
                cur = friend.pop()
                cnt += 1
                
                # 시작점에서 출발해 친구의 dist가 두 보수 지점의 값보다 작으면 dfs 실행
                for i in range(start, size):
                    if pos[i] - pos[start] > cur:
                        cnt = dfs(pos, i, friend, cnt)
                        break

                dist.append(cur)
                return cnt
            
            result = dfs(pos, 0, j, 0)

            # dfs 값이 -1이 아니고 answer도 -1이 아니면 최솟값을 answer로 함
            if result > 0:
                if answer != -1:
                    answer = min(answer, result)
                else:
                    answer = result

    return answer
            
weak =  [1,5,6,10]
dist = [1,2,3,4]
print(solution(12,weak, dist))
    
                

                
                


