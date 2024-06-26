def solution(dirs):
  
    moves = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    visited = set()  
    x, y = 0, 0  

    for dir in dirs:
        nx, ny = x + moves[dir][0], y + moves[dir][1]
       
        if nx < -5 or nx > 5 or ny < -5 or ny > 5:
            continue
        
        visited.add(((x, y), (nx, ny)))
        visited.add(((nx, ny), (x, y)))
        
        x, y = nx, ny

   
    return len(visited) // 2


print(solution("ULURRDLLU"))  
print(solution("LULLLLLLU")) 
