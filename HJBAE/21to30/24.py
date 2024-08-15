"""
각 유저 한 번에 한 명 유저 신고 가능
횟수 제한 X, 서로 다른 유저 계속 신고 가능
여러 번 신고 가능 but, 1회로 처리
k번 이상 신고되면 게시판 이용 정지되고 신고한 모든 유저한테 정지 사실 메일 발송
신고 모든 내용 취합해 한꺼번에 게시판 이용 정지시키고 메일 발송
"""

def solution(id_list, report, k):
    reported_user = {}
    count = {}

    for content in report:
        user_name, reported_name = content.split(" ")
        if reported_name not in reported_user:
            reported_user[reported_name] = {user_name}    # 중복 피하려면 set으로 저장
        else:
            reported_user[reported_name].add(user_name)    # set에서는 .add() 사용

    for user in id_list:
        count[user] = 0
    
    for reported_name, reporters in reported_user.items():
        if len(reporters) >= k:
            for reporter in reporters:
                count[reporter] += 1

    result = list(count.values())

    return result




id_list1 = ["muzi", "frodo", "apeach", "neo"]
report1 = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
k1 = 2
# result1 = [2, 1, 1, 0]

print(solution(id_list1, report1, k1))


id_list2 = ["con", "ryan"]
report2 = ["ryan con", "ryan con", "ryan con", "ryan con"]
k2 = 3
# result2 = [0, 0]

print(solution(id_list2, report2, k2))