# 처음 생각한 방법: 닉네임이 변경되면 이전 기록들의 닉네임 변경
# 시간 복잡도 O(n^2)
def solution_1(record):
    # user에는 id를 키로 받으면 1번째 인덱스에는 닉네임, 2번째 인덱스에는 본인이 기록된 것의 인덱스 저장
    result = []
    user = {} 
    cnt = 0

    for i in record:
        commend = i.split()
        
        if commend[0] == "Enter":
            if commend[1] not in user:  # 신규 유저일 경우
                user[commend[1]] = [commend[2], []]
            else:   # 신규 유저가 아니라면 이전 기록의 닉네임 변경
                past = user[commend[1]][0]
                user[commend[1]][0] = commend[2]
                for i in user[commend[1]][1]:
                    result[i] = result[i].replace(past, user[commend[1]][0])
            
            result.append(user[commend[1]][0] + "님이 들어왔습니다.")
            user[commend[1]][1].append(cnt)
            cnt += 1
            
        elif commend[0] == "Leave":
            result.append(user[commend[1]][0] + "님이 나갔습니다.")
            user[commend[1]][1].append(cnt)
            cnt += 1
        
        elif commend[0] == "Change":
            past = user[commend[1]][0]
            user[commend[1]][0] = commend[2]

            # 이전 자신의 기록들의 닉네임 변경
            for i in user[commend[1]][1]:
                result[i] = result[i].replace(past, user[commend[1]][0])          
    
    return result

# 2번째 방법: 최종적인 id에 대응하는 닉네임을 저장한 후 이를 바탕으로 기록 작성
# 시간복잡도 O(n)
def solution_2(record):
    result = []
    user = {}

    # 각 id의 최종적인 닉네임 결정
    for i in record:
        commend = i.split()

        if commend[0] != "Leave":
            user[commend[1]] = commend[2]
    
    # 최종 닉네임을 바탕으로 기록 작성
    for i in record:
        commend = i.split()

        if commend[0] == "Enter":
            result.append(user[commend[1]] + "님이 들어왔습니다.")
        elif commend[0] == "Leave":
            result.append(user[commend[1]] + "님이 나갔습니다.")
    
    return result

print(solution_1(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
print(solution_2(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
