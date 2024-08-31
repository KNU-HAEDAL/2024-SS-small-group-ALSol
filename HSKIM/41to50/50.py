def is_safe(x, y, stack):
    for dx, dy in stack:
        # 세로줄에 퀸이 있는지 확인
        # 대각선에 퀸이 있는지 확인 (기울기 -1 or 1)
        if dy == y or abs(dx - x) == abs(dy - y):
            return False
    return True

# 백트래킹 함수
def dfs(n, x, stack):
    if x == n:
        return 1

    count = 0
    # 퀸이 n개 -> 모든 가로줄에 퀸이 하나씩 존재
    for y in range(n):
        if is_safe(x, y, stack):
            stack.append((x, y)) # 퀸이 배치된 곳을 스택으로 저장
            count += dfs(n, x + 1, stack)
            stack.pop() # 최근 배치한 퀸 빼기
    
    return count

def solution(n):
    return dfs(n, 0, [])

print(solution(4))
