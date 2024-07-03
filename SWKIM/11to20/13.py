def solution(board, moves):
    stacks = [[] for _ in range(len(board))]
    bucket = []
    cnt = 0

    # board릏 역순으로 탐색해 스택으로 재구성
    for i in range(len(board), 0, -1):
        for j in range(len(board)):
            if board[i-1][j] != 0:
                stacks[j].append(board[i-1][j])
    
    # 꺼낸 인형과 바구니 맨 위에 있는 인형이 같은지 검사
    for i in moves:
        if len(stacks[i-1]) != 0:
            doll = stacks[i-1].pop()

            if len(bucket) != 0 and bucket[-1] == doll:
                bucket.pop()
                cnt += 2
            else:
                bucket.append(doll)
        
    return cnt

# board = [[0, 0, 0, 0, 0], 
#          [0, 0, 1, 0, 3], 
#          [0, 2, 5, 0, 1], 
#          [4, 2, 4, 4, 2], 
#          [3, 5, 1, 3, 1]]
# moves = [1, 5, 3, 5, 1, 2, 1, 4]

# print(solution(board, moves))