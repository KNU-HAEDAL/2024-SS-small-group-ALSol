def solution(board, moves):
    popped_shape_cnt = 0
    moved_shape = 0
    start_list = [[] for _ in range(len(board[0]))]
    end_list = []

    for i in range(len(board) - 1, -1, -1):
        for j in range(len(board[0])):
            if board[i][j]:
                start_list[j].append(board[i][j])

    for k in moves:
        if start_list[k - 1]:
            moved_shape = start_list[k - 1].pop()

            if end_list and end_list[-1] == moved_shape:
                end_list.pop()
                popped_shape_cnt += 2
            else:
                end_list.append(moved_shape)

    return popped_shape_cnt