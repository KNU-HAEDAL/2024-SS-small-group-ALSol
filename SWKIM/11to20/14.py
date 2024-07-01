def solution(n, k, cmd):
    answer = ['O']*n
    cur = k
    trash = []
    
    # index는 현재 데이터를 가리키며 각 인덱스에는 현재 index의 이전과 이후의 index를 가리킨다.
    # 연결 리스트로 구현
    arr = [[i-1, i+1] for i in range(n)]

    for i in cmd:
        i = i.split()   
        if i[0] == 'U':
            for j in range(int(i[1])):
                cur = arr[cur][0]
        
        elif i[0] == 'D':
            for j in range(int(i[1])):
                cur = arr[cur][1]
        
        elif i[0] == 'C':
            before = arr[cur][0]
            next = arr[cur][1]

            trash.append([cur, before, next])
            answer[cur] = 'X'

            # 현재 인덱스가 맨 앞 혹은 맨 뒤인 경우 고려
            # 실제 데이터를 삭제하는 것이 아닌 제외시키는 것
            if before != -1:
                arr[before][1] = next
            if next != n:
                arr[next][0] = before
            
            # 삭제 이후 현재 index의 위치 조정
            if arr[cur][1] != n:
                cur = next
            else:
                cur = before

        elif i[0] == 'Z':
            data = trash.pop()
            answer[data[0]] = 'O'

            # 현재 인덱스가 맨 앞 혹은 맨 뒤인 경우 고려
            # 제외시킨 데이터를 다시 가리키도록 함
            if data[1] != -1:
                arr[data[1]][1] = data[0]
            if data[2] != n:
                arr[data[2]][0] = data[0]

        
    return "".join(answer)
        
    
# print(solution(8, 2, ['C', 'C', 'C', 'C', 'C', 'C', 'Z', 'Z']))
# print(solution(8, 2, ['D 2', 'C', 'U 3', 'C', 'D 4', 'C', 'U 2', 'Z', 'Z', 'U 1', "C"]))