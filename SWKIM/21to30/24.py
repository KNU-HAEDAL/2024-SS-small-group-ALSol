def solution(id_list, report, k):
    # report_dict: key = 신고자, value = 신고한 사람 중 k보다 많이 신고당한 사람의 수
    # report_cnt: key = 신고당한 사람, value = 신고당한 횟수
    report_dict = {x : 0 for x in id_list} 
    report_cnt = {x : 0 for x in id_list}
    
    # set을 활용해 중복된 신고를 제거
    # 신고당한 횟수 구하기
    for i in set(report):
        user = i.split()
        
        report_cnt[user[1]] += 1

    # set을 활용해 중복된 신고를 제거
    # 신고한 사람 중 k번 이상으로 신고당한 사람의 수 구하기
    for i in set(report):
        user = i.split()
        
        if report_cnt[user[1]] >= k:
            report_dict[user[0]] += 1      

    # report_dict의 value 값을 list로 바꾼 뒤 반환
    answer = list(report_dict.values())
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))