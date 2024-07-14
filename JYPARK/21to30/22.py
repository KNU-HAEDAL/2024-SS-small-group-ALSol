def solution(record):
    answer = []
    #해시테이블 작성 id -> key, nickname -> value
    hash_table = dict()
    for i in range(len(record)):
        parts = record[i].split()
        behavior = parts[0]
        id = parts[1]
        if behavior != 'Leave':
            nickname = parts[2]
            hash_table[id] = nickname

    for j in record:
        parts = j.split()
        behavior = parts[0]
        id = parts[1]
        if behavior == 'Enter':
            answer.append('%s님이 들어왔습니다.' %hash_table[id])
        elif behavior == 'Leave':
            answer.append('%s님이 나갔습니다.' %hash_table[id])
        else:
            pass
    return answer


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))