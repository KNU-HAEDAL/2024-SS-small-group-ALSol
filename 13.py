def solution(board, moves):
    answer = 0
    length = len(board[0])
    bucket = [ ]
    stack = [[] for _ in range(length)]

    #board를 stack으로 구현
    for i in range(length - 1, -1, -1):
        for j in range(0, length):
            if board[i][j]:
                stack[j].append(board[i][j])

    for m in moves:
        if stack[m - 1]:
            a =  stack[m - 1].pop()
            if bucket and bucket[-1] == a:
                bucket.pop()
                answer += 2
            else:
                bucket.append(a)
    return answer
    


board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1, 5, 3, 5,1, 2,1, 4]
print(solution(board, moves))
