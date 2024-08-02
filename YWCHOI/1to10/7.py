# <문제 파악>
# (-5, -5), (0, 0) ==> (0, 0), (5, 5) 0~10까지 좌표로 쉽게 파악 가능
# 

def loc(dirs, x, y) :
    if dirs == 'L' :
        x -= 1
    elif dirs == 'R' :
        x += 1
    elif dirs == 'U' :
        y += 1
    elif dirs == 'D' :
        y -= 1
    
    return x, y

def solution(x, y) :
    x, y = 5, 5
    res = set()
    directions = input()
    n = len(directions)

    for i in range(directions):
        x, y = loc(i, x, y)
        if x > 10 and y > 10 and x < -10 and y < -10:
            continue
        else:
            res.add((x, y))
    return len(res) / 2

solution()