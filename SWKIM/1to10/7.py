def solution(dirs):
    roads = []
    curX = 0
    curY = 0
    nextX = 0
    nextY = 0
    cnt = 0

    for i in dirs:
        if i == 'U' and curY < 5:
            nextY += 1            
        elif i == 'L' and curX > -5:
            nextX -= 1            
        elif i == 'D' and curY > -5:
            nextY -= 1                  
        elif i == 'R' and curX < 5:
            nextX += 1               
        else:
            continue

        if [curX, curY, nextX, nextY] not in roads:
            cnt+= 1
            roads.append([curX, curY, nextX, nextY])
            roads.append([nextX, nextY, curX, curY])
        
        curX = nextX
        curY = nextY
        
        
    return cnt