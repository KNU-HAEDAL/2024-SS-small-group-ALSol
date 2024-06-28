def solution(dirs):
    # 음수 제외하고 생각
    x, y = 5, 5
    nx, ny = 0, 0

    path = set()
    for dir in dirs:
        if dir == 'U' and y != 10:
            nx, ny = x, y + 1
        elif dir == 'D' and y != 0:
            nx, ny = x, y - 1
        elif dir == 'L' and x != 0:
            nx, ny = x - 1, y
        elif dir == 'R' and x != 10:
            nx, ny = x + 1, y
        else: 
             continue
        path.add((x, y, nx, ny))
        path.add((nx, ny, x, y))
        x, y = nx, ny

    return len(path)/2

d = 'ULURRDLLU'
print(solution(d))