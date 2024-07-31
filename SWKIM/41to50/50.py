# 세로줄에 퀸이 있는지 확인하는 함수
def is_col(y, stack):
    for pos in stack:
        if pos[1] == y:
            return True
    
    return False

# 대각선에 퀸이 있는지 확인하는 함수
def is_diagonal(x, y, stack):
    for dx, dy in stack:
        res = (dy - y) / (dx - x)
        # 기울기가 1 또는 -1이면 퀸이 대각선에 존재함
        if res == 1 or res == -1:
            return True
    
    return False

# 백트래킹 함수
def dfs(n, cnt, start_x, stack, answer):    
    # 퀸이 모두 배치되면 답에 1 더함
    if cnt == n:
        return answer + 1

    # 퀸이 n개이므로 모든 가로줄에 퀸이 하나씩 존재하는 것을 이용
    for y in range(n):
        # 세로 또는 대각선에 퀸이 있는지 확인
        if not(is_col(y, stack) or is_diagonal(start_x, y, stack)):
            stack.append([start_x, y])  # 퀸이 배치된 곳을 스택으로 저장
            answer = dfs(n, cnt+1, start_x+1, stack, answer)
            stack.pop() # 최근 배치한 퀸 빼기

    return answer

def solution(n):
    answer = 0
    stack = []
    answer = dfs(n, 0, -1, stack, answer)
    return answer

print(solution(12))