def solution(places):
    answer = []


    for p in places:
        people = []

        # 사람이 있는 위치 찾기
        for i in range(5):
            for j in range(5):
                if p[i][j] == 'P':
                    people.append([i, j])
        
        # 거리두기를 지켰는지 확인
        check = True

        # 각 사람들의 거리를 비교
        while people:
            x, y = people.pop()

            for r, c in people:
                # 거리가 2인 경우 파티션으로 가리지 못했다면 거리두기 실패
                if abs(x-r) + abs(y-c) == 2:
                    if x != r and y != c:
                        if (p[x][c] == 'O' or p[r][y] == 'O'):
                            check = False
                    elif x == r and p[x][min(y, c) + 1] == 'O':
                        check = False
                    elif y == c and p[min(x, r) + 1][y] == 'O':
                        check = False
                # 거리가 2보다 작으면 거리두기 실패
                elif abs(x-r) + abs(y-c) < 2:
                    check = False
        
        # 거리두기에 성공했다면 1, 아니면 0
        if check:
            answer.append(1)
        else: 
            answer.append(0)
    return answer