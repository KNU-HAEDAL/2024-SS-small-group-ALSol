# 13번
"""
크레인 인형 뽑기 기계
게임화면 1x1 크기 격자 NxN 위쪽에는 크레인 오른쪽에는 바구니
크레인 좌우로 움직일 수 있고 크레인 멈춘 위치에서 가장 위에 있는 인형 집어올릴 수 있음
같은 인형 두개 연속 쌓이면 펑 하고 사라짐
바구니는 충분히 큼
"""
def solution(board, moves):
    basket = []  # 뽑은 인형 담는 바구니
    answer = 0   # 사라진 인형 개수
    
    for move in moves:
        column = move - 1  # 크레인 1부터 시작인데 배열은 0부터 시작하니까 집게 의미하는 move는 0번쨰 column부터 시작하니까 -1 해줘야 함
        for row in range(len(board)):
            if board[row][column] != 0:  # 0이 아닌 경우(인형이 있는 경우)
                if basket and basket[-1] == board[row][column]:
                    basket.pop()  # 같은 인형 연속 -> 제거
                    answer += 2   # 제거된 인형은 2개니까 answer += 2
                else:
                    basket.append(board[row][column])  # 뽑은 인형 basket에 추가
                board[row][column] = 0  # 인형 뽑은 자리는 0으로 만듦
                break  # 다음 move로 이동
    return answer

#예시
board = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 3],
    [0, 2, 5, 0, 1],
    [4, 2, 4, 4, 2],
    [3, 5, 1, 3, 1]
]

moves = [1, 5, 3, 5, 1, 2, 1, 4]
print(solution(board, moves))  # 출력값 4

# 4(3(11)3)2x4 > 4개 사라지고 basket = [4, 2, 4]
"""
00000
00103
02501
42442
35131
"""