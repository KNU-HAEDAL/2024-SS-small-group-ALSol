def solution(id_list, report, k):
    answer = []
    report_id = { }
    report_num = { }
    
    #id를 키로한 해시 테이블, value에는 리스트가 들어갈 것임.
    for id in id_list:
        if id not in report_id:
            report_id[id] = [ ]
            report_num[id] = 0

    #신고한 id들을 리스트에 저장. reprt_num은 id를 키로하고 신고당한 횟수를 값으로 하는 딕셔너리
    for i in report:
        id, reported_id = i.split()
        if reported_id not in report_id[id]:
            report_id[id].append(reported_id)
            report_num[reported_id] += 1
    
    #k번 이상 신고당한 유저를 담을 리스트
    count = [ ]
    for id in report_num:
        if report_num[id] >= k:
            count.append(id)

    #id별로 받을 메일 개수 계산
    a = set(count)
    for id in report_id:
        b = set(report_id[id])
        mail_num = len(a.intersection(b))
        answer.append(mail_num)
    return answer



#id_list = ["muzi", "frodo", "apeach", "neo"]
#report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 3
id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
print(solution(id_list, report, k))