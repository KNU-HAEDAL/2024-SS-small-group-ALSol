def solution(record):
    user_id = { }
    answer = [ ]

    for i in record:
        command = i.split(" ")

        if command[0] != "Leave":
            user_id[command[1]] = command[2]

        for i in record:
            command = i.split(" ")
            if command[0] == "Enter":
                answer.append("%s님이 들어왔습니다." % user_id[command[1]])

            elif command[0] == "Change":
                pass

            else:
                answer.append("%s님이 나갔습니다." % user_id[command[1]])

    return answer