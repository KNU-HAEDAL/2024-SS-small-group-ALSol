def solution(arr):
    answer = [0, 0]
    n = len(arr)
    
    # quad 트리 형태로 압축
    def quad(x, y, r, c):
        result = set()
        
        # 0 또는 1로만 이루어져 있는지 확인
        for i in range(x, r):
            for j in range(y, c):
                result.add(arr[i][j])
                if len(result) == 2:
                    break
        # 0, 1 중 하나만 존재하는 경우
        if len(result) != 2:
            num = result.pop()
            answer[num] += 1
        
        # 0, 1이 모두 존재하는 경우
        # 4개로 쪼개어 다시 압축
        quad(x, y, (x+r)//2, (y+c)//2)
        quad(x, (y+c)//2, (x+r)//2, c)
        quad((x+r)//2, y, r, (y+c)//2)
        quad((x+r)//2, (y+c)//2, r, c)
    
    quad(0,0,n,n)

    return answer

arr = [[1,1, 0, 0], [1, 0, 0, 0], [1, 0, 0,1], [1,1,1,1]]
print(solution(arr))

    
            
            