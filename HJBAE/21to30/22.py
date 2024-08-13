"""
채팅방에 누군가 들어오면 "[닉네임] 님이 들어왔습니다."
채팅방에 누군가 나가면 "[닉네임] 님이 나갔습니다."
닉네임 변경하는 두 가지 방법
1. 채팅방 나간 후, 새로운 닉네임으로 다시 들어감
2. 채팅방에서 닉네임 변경
닉네임 변경 시 기존 출력되어 있던 메시지 닉네임도 전부 바뀜
중복 닉네임 허용
채팅방에 들어오고 나가거나 닉네임을 변경한 기록이 담긴 문자열 배열 record
-> 모든 기록이 처리된 다음 최종으로 방을 개설한 사람이 보는 메시지를 문자열 배열 형태로 반환
"""

def solution(record):
    user_info = {}
    chat_log = []
    for i in range(len(record)):
        chat_log.append(record[i].split(" "))
    print(chat_log)

    for i in range(len(chat_log)):
        if (chat_log[i][0] in ("Enter", "Change")):
            user_info[chat_log[i][1]] = chat_log[i][2]
        elif chat_log[i][0] == "Leave":
            pass
        else:
            print("대화 기록이 이상하네용..")
    
    result = []
    for i in range(len(chat_log)):
        if chat_log[i][0] == "Enter":
            result.append(f"{user_info[chat_log[i][1]]}님이 들어왔습니다.")
        elif chat_log[i][0] == "Leave":
            result.append(f"{user_info[chat_log[i][1]]}님이 나갔습니다.")

    return result

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
# result = ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다"]

print(solution(record))

# Enter uid1234 Muzi
# Enter uid4567 Prodo
# Leave uid1234
# Enter uid1234 Prodo
# Change uid4567 Ryan