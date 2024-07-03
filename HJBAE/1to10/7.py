def solution(dirs):
    current_position = (0, 0)   #시작 위치
    move = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}   #이동 케이스
    
    visited_paths = set()
    for direction in dirs:
        
        x, y = current_position
        dx, dy = move[direction]
        new_position = (x + dx, y + dy)
        
        if -5 <= new_position[0] <= 5 and -5 <= new_position[1] <= 5:   #이동 가능 범위
            visited_paths.add((current_position, new_position))
            visited_paths.add((new_position, current_position))
            # 양방향 저장? 중복방지
            current_position = new_position    #위치 업데이트
    
    # 방문한 길의 개수는 절반으로 나누어 반환
    return len(visited_paths) // 2


print(solution("ULULLRULU"))  # 출력: 8
print(solution("LURRLLLLU"))  # 출력: 7


"""
set 자료형은 중복된 값을 허용하지 않음 > 동일한 길 지나더라도 하나의 값으로 저장 가능
"""