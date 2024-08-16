def solution(id_list, report, k):
    user = {}
    count = {}

    for i in report:
        user_id, reported_id = i.split()
        if reported_id not in user:
            user[reported_id] = set()
        user[reported_id].add(user_id)
    
    for reported_id, user_id_lst in user.items():
        if len(user_id_lst) >= k:
            for uid in user_id_lst:
                if uid not in count:
                    count[uid] = 1
                else:
                    count[uid] += 1
    
    answer = []
    for i in range(len(id_list)):
        if id_list[i] not in count:
             answer.append(0)
        else:
            answer.append(count[id_list[i]])
    
    return answer