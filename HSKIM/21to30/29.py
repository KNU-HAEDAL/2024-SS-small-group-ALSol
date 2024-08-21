def solution(enroll, referral, seller, amount):
    parent = dict(zip(enroll, referral))

    total = {name: 0 for name in enroll}

    for i in range(len(seller)):
        money = amount[i] * 100
        cur_name = seller[i]

        while money > 0 and cur_name != "-":
            total[cur_name] += money - money // 10
            cur_name = parent[cur_name]

            money //= 10
    
    return [total[name] for name in enroll]


# enroll = ['john', 'mary', 'edward', 'sam' , 'emily' , 'jaimie' ,'tod', 'young']
# referral = ['-', '-', 'mary', 'edward', 'mary', 'mary', 'jaimie', 'edward']
# seller = ['young', 'john', 'tod', 'emily', 'mary']
# amount = [12, 4, 2, 5, 10]
# print(solution(enroll, referral, seller, amount))