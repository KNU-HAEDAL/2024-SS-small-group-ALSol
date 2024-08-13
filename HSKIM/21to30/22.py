def solution(record):
    answer = []
    uid = {}

    for str in range(len(record)):
        cmd = str.split(" ")
        if cmd[0] == "Enter" or cmd[0] == "Change":
            uid[cmd[1]] = cmd[2]
    
    for str in range(len(record)):
        cmd = str.split(" ")
        if cmd[0] == "Enter":
            answer.append("%s님이 들어왔습니다." % uid[cmd[1]])
        elif cmd[0] == "Leave":
            answer.append("%s님이 나갔습니다." % uid[cmd[1]])
    
    return answer

