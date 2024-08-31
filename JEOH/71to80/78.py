def solution(board):
    row,col=len(board),len(board[0])
    for i in range(1,row):
        for j in range(1,col):
            if board[i][j]==1:
                up,left,ul=(
                    board[i-1][j],
                    board[i][j-1].
                    board[i-1][j-1]
                )
                board[i][j]=min(up,left,ul)+1
    a=max(max(x) for x in board)
    return a**2