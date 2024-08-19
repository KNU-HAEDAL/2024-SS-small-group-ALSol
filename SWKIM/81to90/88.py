def solution(today, terms, privacies):
    answer = []
    data = {}

    # today 정수로 변환
    cur_y = int(today[0:4])
    cur_m = int(today[5:7])
    cur_d = int(today[8:10])

    # dict을 활용해 term 저장
    for info in  terms:
        t, n = info.split()
        data[t] = int(n)

    for i in range(len(privacies)):
        # privacies에서 년, 월, 일, term을 받아 저장
        y = int(privacies[i][:4])
        m = int(privacies[i][5:7])
        d = int(privacies[i][8:10]) - 1
        t = privacies[i][-1]

        # 보관 기간만큼 더하기
        m += data[t]

        while m > 12:
            y += 1
            m -= 12
        
        # 보관 기관과 today를 비교해 지났다면 answer에 추가
        if y < cur_y:
            answer.append(i+1)
        elif y == cur_y and m < cur_m:
            answer.append(i+1)
        elif y == cur_y and m == cur_m and d < cur_d:
            answer.append(i+1)


    
    return answer

